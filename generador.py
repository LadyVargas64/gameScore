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

    def generaTable(self, itemTable):
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