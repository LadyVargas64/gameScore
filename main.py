import cherrypy, os
import generador
import csv


class goodAndDevil(object):
    @cherrypy.expose
    def index(self):
        rnk = open("public/item.csv", "r")
        lgr = open("public/item.csv", "r")
        inf = open("public/item.csv", "r")

        miGenerador = generador.Generador()
        miGenerador2 = generador.Generador()
        miGenerador3 = generador.Generador()

        tabla = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>G&D</title>
    <link href="static/css/bootstrap.min.css" rel="stylesheet">
    <link href="static/css/stylish-portfolio.css" rel="stylesheet">
    <link href="static/css/student.css" rel="stylesheet">
    <link href="static/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">
</head>
<body>
    <a id="menu-toggle" href="#" class="btn btn-dark btn-lg toggle"><i class="fa fa-bars"></i></a>
    <nav id="sidebar-wrapper">
        <ul class="sidebar-nav">
            <a id="menu-close" href="#" class="btn btn-light btn-lg pull-right toggle"><i class="fa fa-times"></i></a>
            <li class="sidebar-brand">
                <a href="#top" onclick=$("#menu-close").click();>Good and Devil</a>
            </li>
            <li>
                <a href="#top" onclick=$("#menu-close").click();>Home</a>
            </li>
        </ul>
    </nav>
    <!-- Header -->
    <header id="top" class="header">
        <div class="text-vertical-center">
            <h1>GOOD &amp; DEVIL</h1>
            <!-- <h3>A Game for known your Real Personality</h3> -->
            <br>
            <a href="#about" class="btn btn-dark btn-lg">Coming soon</a>
        </div>
    </header>
        <!-- About -->
        <section id="about" class="about">
            <div class="container">
                <div class="row">
                    <div class="col-lg-12 text-center">
                    <div class="wrap">
                    <div id="TabbedPanels1" class="TabbedPanels">
                            <ul class="TabbedPanelsTabGroup">
                                <li class="TabbedPanelsTab itm1" tabindex="0">Ranking</li>
                                <li class="TabbedPanelsTab itm2" tabindex="0">Logros</li>
                                <li class="TabbedPanelsTab itm3" tabindex="0">Perfil</li>
                            </ul>
                            <div class="TabbedPanelsContentGroup">
                                
                                    [ CONT1 ]
                                    
                                    [ CONT2 ]   
                                
                                    [ CONT3 ]
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                <!-- /.row -->
            </div>
            <!-- /.container -->
        </section>
    <!-- jQuery -->
<script src="static/js/jquery.js"></script>
<!-- Bootstrap Core JavaScript -->
<script src="static/js/bootstrap.min.js"></script>
<script src="static/js/SpryTabbedPanels.js"></script>
<script type="text/javascript"> var TabbedPanels1 = new Spry.Widget.TabbedPanels("TabbedPanels1"); </script>
<!-- Custom Theme JavaScript -->
<script>
// Trae el nombre del jugador seleccionado
$( ".rnk" ).click(function() { 
	var oID = $(this).attr("id");  
	var num = $('#'+oID+' .ps').text();
	
	$('.jug').hide();
    $('.jug'+num).show();
    
    $('.info_jug').hide();
    $('.info_jug'+num).show();
    
    $(".TabbedPanelsTab").removeClass( "TabbedPanelsTabSelected" )
    $(".itm2").addClass("TabbedPanelsTabSelected")
    
    $(".TabbedPanelsContent").removeClass( "TabbedPanelsContentVisible" )
    $(".logros ").addClass("TabbedPanelsContentVisible")
    
    $('.ranking').hide();
    $('.logros').show();

});

// Closes the sidebar menu
$("#menu-close").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggleClass("active");
});
// Opens the sidebar menu
$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#sidebar-wrapper").toggleClass("active");
});
// Scrolls to the selected menu item on the page
$(function() {
    $('a[href*=#]:not([href=#],[data-toggle],[data-target],[data-slide])').click(function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });
});
//#to-top button appears after scrolling
var fixed = false;
$(document).scroll(function() {
    if ($(this).scrollTop() > 250) {
        if (!fixed) {
            fixed = true;
            // $('#to-top').css({position:'fixed', display:'block'});
            $('#to-top').show("slow", function() {
                $('#to-top').css({
                    position: 'fixed',
                    display: 'block'
                });
            });
        }
    } else {
        if (fixed) {
            fixed = false;
            $('#to-top').hide("slow", function() {
                $('#to-top').css({
                    display: 'none'
                });
            });
        }
    }
});
// Disable Google Maps scrolling
// See http://stackoverflow.com/a/25904582/1607849
// Disable scroll zooming and bind back the click event
var onMapMouseleaveHandler = function(event) {
    var that = $(this);
    that.on('click', onMapClickHandler);
    that.off('mouseleave', onMapMouseleaveHandler);
    that.find('iframe').css("pointer-events", "none");
}
var onMapClickHandler = function(event) {
        var that = $(this);
        // Disable the click handler until the user leaves the map area
        that.off('click', onMapClickHandler);
        // Enable scrolling zoom
        that.find('iframe').css("pointer-events", "auto");
        // Handle the mouse leave event
        that.on('mouseleave', onMapMouseleaveHandler);
    }
    // Enable map zooming with mouse scroll when the user clicks the map
$('.map').on('click', onMapClickHandler);
</script>
</body>
</html>
"""
        rep = tabla.replace('[ CONT1 ]', miGenerador.generaTable(rnk))\
            .replace('[ CONT2 ]', miGenerador.generaLogros(lgr))\
            .replace('[ CONT3 ]', miGenerador.generaInformacion(inf))
        return rep



if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.config.update({'server.socket_host': '127.0.0.1', })
    cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')), })
    cherrypy.quickstart(goodAndDevil(), '/', conf)
