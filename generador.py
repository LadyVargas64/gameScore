class Generador:
    def generaTitPar(self, titulo, parrafo):
        titulo = "<h1>" + titulo + "</h1>"
        parrafo = "<p>" + parrafo + "</p>"
        return titulo + parrafo

    def generaLista(self, listaItems):
        codigo = ""
        for i in listaItems:
            codigo = codigo + "<li>" + i + "</li>"
        return "<ol>" + codigo + "</ol>"

    def generaTabls(self, itemTable):
        table=""
        td = ""
        for i in itemTable:
            tr1 = "<tr>"
            for j in i.split(","):
                td = td + "<td>" + j + "</td>"
            tr2 = "</tr>"

            table = table + tr1 + td + tr2
            td = ""
        return "<table>" + table + "</table>"

    def generaTable(self, itemTable):
        con = ''
        x = 1
        table=""
        td = ""
        for p,i in enumerate(itemTable):

            pst = ''
            if(x <= 3):
                pst = 'pst'+ str(x)
                x = x + 1

            tr1 = "<div class ='rnk'>" \
                    "<div class ='pst "+pst+"' ></div>" \
                    "<div class ='dtl' >" \
                        "<p class='ps'>" +str(p+1)+ "</p>" \
                    "</div>"
            for j in i.split(","):
                td = td + "<div>" + j + "</div>"
            tr2 = "</div>"

            table = table + tr1 + td + tr2
            td = ""

        return "<div  class='TabbedPanelsContent'>" + table + "</div>"