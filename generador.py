class Generador:
    def generaTable(self, itemTable):
        x = 1
        table=""
        td = ""
        con = 0
        lista=[]
        b = 0
        for p,i in enumerate(itemTable):
            pst = ''
            if(x <= 3):
                pst = 'pst'+ str(x)
                x += 1
            con += 1
            tr1 = "<div class ='rnk' id='con"+str(con)+"'>" \
                    "<div class ='pst "+pst+"' ></div>" \
                    "<div class ='dtl' >" \
                        "<p class='ps'>" +str(p+1)+ "</p>" \

            lista.append([])

            for j in i.split(","):
                lista[b].append(j)

            td = td + "<p class='nm'> " + str(lista[b][0]) + " </p></div><div class='nvl'> <p> Nv. " + str(lista[b][1]) + " </p></div><div class='pnt'> <p> Pts: " + str(lista[b][2]) + "</p></div>"
            b += 1
            table = table + tr1 + td + "</div>"
            td = ""
        return "<div  class='TabbedPanelsContent ranking'>" + table +"</div>"
    def generaLogros(self, itemTable):
        lista = []
        b = 0
        lg = ''
        v = 0
        for p, i in enumerate(itemTable):
            lista.append([])
            for j in i.split(","):
                lista[b].append(j)
            v += 1
            td = "" \
                "<div class='jug jug"+str(v)+"'>"\
                    "<h1>"+ str(lista[b][0]) +"</h1>"\
                    "<div class='ach lv1'> \
                        <div class='cl c1 est"+str(lista[b][3])+"'><div class='tooltips'><span class='tooltiptexts'>logro 1</span></div></div>\
                        <div class='cl c2 est"+str(lista[b][4])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 2</span></div></div>\
                        <div class='cl c3 est"+str(lista[b][5])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 3</span></div></div>\
                    </div>\
                    <div class='ach lv2'>\
                        <div class='cl c1 est"+str(lista[b][6])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 4</span></div></div>\
                        <div class='cl c2 est"+str(lista[b][7])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 5</span></div></div>\
                        <div class='cl c3 est"+str(lista[b][8])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 6</span></div></div>\
                    </div>\
                    <div class='ach lv3'>\
                        <div class='cl c1 est"+str(lista[b][9])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 7</span></div></div>\
                        <div class='cl c2 est"+str(lista[b][10])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 8</span></div></div>\
                        <div class='cl c3 est"+str(lista[b][11])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 9</span></div></div>\
                    </div>\
                    <div class='ach lv4''>\
                        <div class='cl c1 est"+str(lista[b][12])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 10</span></div></div>\
                        <div class='cl c2 est"+str(lista[b][13])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 11</span></div></div>\
                        <div class='cl c3 est"+str(lista[b][14])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 12</span></div></div>\
                    </div>\
                    <div class='ach lv5'>\
                        <div class='cl c1 est"+str(lista[b][15])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 13</span></div></div>\
                        <div class='cl c2 est"+str(lista[b][16])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 14</span></div></div>\
                        <div class='cl c3 est"+str(lista[b][17])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 15</span></div></div>\
                    </div>\
                    <div class='ach lv6'>\
                        <div class='cl c1 est"+str(lista[b][18])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 16</span></div></div>\
                        <div class='cl c2 est"+str(lista[b][19])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 17</span></div></div>\
                        <div class='cl c3 est"+str(lista[b][20])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 18</span></div></div>\
                    </div>\
                    <div class='ach lv7''>\
                        <div class='cl c1 est"+str(lista[b][21])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 19</span></div></div>\
                        <div class='cl c2 est"+str(lista[b][22])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 20</span></div></div>\
                        <div class='cl c3 est"+str(lista[b][23])+"''><div class='tooltips'><span class='tooltiptexts'>Logro 21</span></div></div>\
                    </div>"\
                "</div>"
            lg = lg + td
            b += 1
        return "<div  class='TabbedPanelsContent logros'>" + lg +"</div>"
    def generaInformacion(self, itemTable):
        lista = []
        b = 0
        lg = ''
        v = 0
        for p, i in enumerate(itemTable):
            lista.append([])
            for j in i.split(","):
                lista[b].append(j)
            v += 1
            td = "<div class='info_jug info_jug"+str(v)+"'><div class='foto'></div><div class='info'>\
                    <div class='lvl'>Nivel "+str(lista[b][1])+"</div><div class='xp'>"+str(lista[b][30])+" / 10000 XP</div>\
                    <h2 class='cont'>Nombre</h2><p class='res'>"+ str(lista[b][0]) +"</p>\
                    <h4 class='cont'>Rango</h4><p class='res'>"+ str(lista[b][24]) +"</p>\
                    <h4 class='cont'>Edad</h4><p class='res'>"+ str(lista[b][25]) +"</p>\
                    <h4 class='cont'>Fecha de Cumpleanos</h4><p class='res'>"+ str(lista[b][26]) +"</p>\
                    <h4 class='cont'>Genero</h4><p class='res'>"+ str(lista[b][27]) +"</p>\
                </div>\
                <div class='info_gm'>\
                    <h4 class='cont'>Partidas Ganadas</h4><p class='res'>"+ str(lista[b][28]) +"</p>\
                    <h4 class='cont'>Partidas Perdidas</h4><p class='res'>"+ str(lista[b][29]) +"</p>\
                    <h4 class='cont'>Mayor Puntaje</h4><p class='res'>"+ str(lista[b][2]) +"</p>\
                </div></div>"
            lg = lg + td
            b += 1
        return "<div  class='TabbedPanelsContent info_gen'>" + lg +"</div>"