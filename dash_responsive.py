import dash

class Dash_responsive(dash.Dash):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    #Overriding from https://github.com/plotly/dash/blob/master/dash/dash.py#L282
    def index(self, *args, **kwargs):
        scripts = self._generate_scripts_html()
        css = self._generate_css_dist_html()
        config = self._generate_config_html()
        title = getattr(self, 'title', 'Dash')
        return ('''
        <!DOCTYPE html>
        <html prefix="og: http://ogp.me/ns#">
            <head>
                <meta property="og:title" content="{}"/>
                <meta property="og:url" content="https://stubhub-listings.herokuapp.com"/>
                <meta property="og:description"
                  content="This app enables you to download all stubhub listings for a given event id."/>
                <meta name="og:image" content="https://cdn.rawgit.com/KobaKhit/stubhubAPI/dc4969bc/readme_plots/heatmap.png"/>
                <title>{}</title>
                {}
            </head>
            <body>
                <div id="react-entry-point">
                    <div class="_dash-loading">
                        Loading Stubhub Listings...
                    </div>
                </div>
            </body>
            <footer>
                {}
                {}
            </footer>
        </html>
        '''.format(title,title, css, config, scripts))