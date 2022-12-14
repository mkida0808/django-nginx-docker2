from rest_framework.response import Response
import json
from app.models.testtable import testtable
from rest_framework import viewsets
from rest_framework.decorators import action

class seinotest(viewsets.ViewSet):
    @action(methods=['get'], detail=False)
    def get(self, request):

        retdata = testtable.objects.all().order_by('col1')[:10000]
        ret = []
        for obj in retdata:

            ret.append({
                'col1':str(obj.col1),
                'col2':obj.col2,
                'col3':str(obj.col3),
                'col4':obj.col4,
                'col5':obj.col5,
                'col6':obj.col6,
                'col7':obj.col7,
                'col8':str(obj.col8),
                'col9':obj.col9,
                'col10':obj.col10,
                'col11':obj.col11,
                'col12':obj.col12,
                'col13':obj.col13,
                'col14':obj.col14,
                'col15':obj.col15,
                'col16':obj.col16,
                'col17':obj.col17,
                'col18':obj.col18,
                'col19':obj.col19,
                'col20':obj.col20,                
            })
            
            '''
                'col11':obj.col11,
                'col12':obj.col12,
                'col13':obj.col13,
                'col14':obj.col14,
                'col15':obj.col15,
                'col16':obj.col16,
                'col17':obj.col17,
                'col18':obj.col18,
                'col19':obj.col19,
                'col20':obj.col20,
                'col21':obj.col21,
                'col22':obj.col22,
                'col23':obj.col23,
                'col24':obj.col24,
                'col25':obj.col25,
                'col26':obj.col26,
                'col27':obj.col27,
                'col28':obj.col28,
                'col29':obj.col29,
                'col30':obj.col30,
                'col31':obj.col31,
                'col32':obj.col32,
                'col33':obj.col33,
                'col34':obj.col34,
                'col35':obj.col35,
                'col36':obj.col36,
                'col37':obj.col37,
                'col38':obj.col38,
                'col39':obj.col39,
                'col40':obj.col40,
                'col41':obj.col41,
                'col42':obj.col42,
                'col43':obj.col43,
                'col44':obj.col44,
                'col45':obj.col45,
                'col46':obj.col46,
                'col47':obj.col47,
                'col48':obj.col48,
                'col49':obj.col49,
                'col50':obj.col50,
                'col51':obj.col51,
                'col52':str(obj.col52),
                'col53':str(obj.col53),
                'col54':obj.col54,
                'col55':obj.col55,
                'col56':obj.col56,
                'col57':obj.col57,
                'col58':obj.col58,
                'col59':str(obj.col59),
                'col60':obj.col60,
                'col61':str(obj.col61),
                'col62':obj.col62,
                'col63':obj.col63,
                'col64':obj.col64,
                'col65':obj.col65,
                'col66':obj.col66,
                'col67':obj.col67,
                'col68':obj.col68,
                'col69':obj.col69,
                'col70':obj.col70,
                'col71':obj.col71,
                'col72':obj.col72,
                'col73':obj.col73,
                'col74':obj.col74,
                'col75':obj.col75,
                'col76':obj.col76,
                'col77':obj.col77,
                'col78':obj.col78,
                'col79':obj.col79,
                'col80':obj.col80,
                'col81':obj.col81,
                'col82':obj.col82,
                'col83':obj.col83,
                'col84':obj.col84,
                'col85':obj.col85,
                'col86':obj.col86,
                'col87':obj.col87,
                'col88':obj.col88,
                'col89':obj.col89,
                'col90':obj.col90,
                'col91':obj.col91,
                'col92':obj.col92,
                'col93':obj.col93,
                'col94':str(obj.col94),
                'col95':obj.col95,
                'col96':obj.col96,
                'col97':obj.col97,
                'col98':str(obj.col98),
                'col99':obj.col99,
                'col100':obj.col100,
                'col101':obj.col101,
            '''
        return Response(json.dumps(ret))