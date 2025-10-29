from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtCore import QUrl
from urllib.parse import urlparse, parse_qs


""" These filters might seem obscene or vulgar , but these are important for a safe web experience for kids and also helpful for
not ruining your life .... Tip => Dont check KEYWORDS and BLOCKED_DOMAINS unless contributing."""


html = """
<html>
    <head>
        <style>
            body {
                background-color: #121212;
                color: #e0e0e0;
                font-family: 'Segoe UI', Roboto, Arial, sans-serif;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background-color: #1e1e1e;
                border-radius: 12px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
                padding: 40px 60px;
                text-align: center;
                transition: transform 0.3s ease;
            }
            .card:hover {
                transform: scale(1.03);
            }
            h2 {
                color: #ff4c4c;
                font-size: 32px;
                margin-bottom: 20px;
                text-shadow: 0 0 8px rgba(255, 76, 76, 0.5);
            }
            p {
                color: #cccccc;
                font-size: 18px;
                line-height: 1.5;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🚫 Blocked Search</h2>
            <p>Your search contains blocked keywords or Domain.<br>
            Please revise your query and url, then try again.</p>
        </div>
    </body>
</html>
"""

KEYWORDS = [
    "porn", "sex", "erotic", "nudity", "xxx", "adult", "hentai", "fetish", "webcam sex", "pornographic",
    "hardcore", "nsfw", "orgasm", "masturbation", "pornstar", "strip", "voyeurism", "bdsm", "fetishism", 
    "s&m", "breast", "butt", "genital", "penis", "vagina", "nipple", "anal", "hardcore", "amateur", 
    "milf", "cum", "gay", "lesbian", "blowjob", "dildo", "bukkake", "fisting", "dominatrix",
    "oral sex", "sex toys", "cuckold", "furry", "sex tape", "sex video", "adult film", "porn video",
    "nude", "sex cam", "camgirl", "camboy", "sex worker", "xxx videos", "adult streaming", "erotic story",
    "xx", "live porn", "nude model", "exotic dancer", "stripping", "escort", "hooker", "prostitute",
    "sex shop", "escort service", "sex services", "adult chat", "stripper", "masturbate", "oral", "hard-on",
    "shemale", "transgender", "intercourse", "orgy", "sex addict", "porn addiction", "kink", 
    "voyeur", "pornography", "pussy", "cumshot", "cock","suck", "buttplug", "dildo", "vibrator", "sex fantasy", "lube", "condom", "dirty talk", "pillow humping","tease", "striptease", "sexting", "dominant", "submissive", "anal play", 
    "slut", "whore", "bimbo", "horny", "sex tape leak", "sex scandal", "erotic roleplay","squirt","creampie","camel toe"
    "adult dating", "sexual harassment", "seduction", "flirting", "sex ad", "adult games", "porn blog", 
    "sexual content", "adult entertainment", "adult clips", "hardcore porn", "adult videos", "explicit","desi","mms","boobs", "naked","spank","gilf","hot girl","hot women","hot model","teen porn","girl showing","bikini","panty","bra","xx"
]

BLOCKED_DOMAINS = [
    "pornhub.com", "xvideos.com", "xhamster.com", "youporn.com", "brazzers.com", "redtube.com", 
    "chaturbate.com", "onlyfans.com", "camsoda.com", "spankwire.com", "hentaifoundry.com", "fakku.net",
    "bdsm.com", "myfreecams.com", "livejasmin.com", "livecamgirls.com", "bongacams.com", "cam4.com", 
    "camgirl.com", "shemale.com", "gayporn.com", "amateurporn.com", "tnaflix.com", "tube8.com", 
    "pornostar.com", "sex.com", "pornstarplanet.com", "fapdu.com", "xtube.com", "meetyourheroes.com",
    "dirtyroulette.com", "eroticmature.com", "fetlife.com", "adultfriendfinder.com", "sexsearch.com",
    "adultmatchmaker.com", "adultsearch.com", "naked.com", "erotica.com", "sexchat.com", "nudeweb.com",
    "hentaimama.com", "porno.com", "sexcam.com", "sexkittens.com", "sexlovers.com", "playboy.com","eporner.com",
    "teenxy.com","kamababa.desi","nakedgirls.com", "nudeart.com", "xxxtentacion.com", "bustybabe.com", "camgirl.com", "tubepornclassic.com","spankbang.com","pornhat.com"
]



def registered_domain(hostname: str) -> str | None:
    if not hostname:
        return None
    parts = hostname.split('.')
    return '.'.join(parts[-2:]) if len(parts) >= 2 else hostname


class FilterPage(QWebEnginePage):
    def acceptNavigationRequest(self, url: QUrl, nav_type, isMainFrame: bool):
       
        if not isMainFrame:
            return super().acceptNavigationRequest(url, nav_type, isMainFrame)

        parsed = urlparse(url.toString())
        domain = registered_domain(parsed.hostname or "")
        qs = parse_qs(parsed.query)
        search_term = qs.get("q", [""])[0].lower()

        #print(f"→ Navigating to {domain}, search={search_term!r}", flush=True)


        if domain in BLOCKED_DOMAINS or any(k in str(domain) for k in KEYWORDS):
            self.setHtml(html)
            return False


        if domain in ("google.com", "bing.com", "duckduckgo.com", "yahoo.com","brave.com"):
            if any(k in search_term for k in KEYWORDS):
                self.setHtml(html)
                return False

        # otherwise allow navigation
        return super().acceptNavigationRequest(url, nav_type, isMainFrame)

