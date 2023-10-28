import json
import re

import json2table

from markupsafe import Markup

def fmt(m):
    t=m.group()
    try:
        t=float(t)
        return f"{t:.2f}%"
    except:
        pass
    return t


def format_json(objs,ex=False):
    try:
        if objs:
            objs = objs[0]
        try:
            del objs["region"]
        except:
            pass
        if objs and "emotion" in objs:
            objs["emotion <br/>(based on <br/>facial Expression)"] = objs["emotion"]
            del objs["emotion"]
            dominantemotion = objs["dominant_emotion"]
            del objs["dominant_emotion"]
            objs["dominant_emotion"] = dominantemotion
        infoFromJson = objs
        build_direction = "LEFT_TO_RIGHT"
        table_attributes = {"style": "width:90%;border-collapse:collapse;", "class":"data-table"}
        image_result = json2table.convert(infoFromJson,
                                 build_direction=build_direction,
                                 table_attributes=table_attributes)
        image_result = re.sub(r'e-\d+', "0.00", image_result)
        image_result = re.sub(r'-?\d+\.\d+', fmt, image_result)
        if ex:
            styles = """
            <style>
            .data-table td{border:1px solid #ccc;padding:5px}
            .data-table th{border:1px solid #ccc;background-color: #ddd;padding:5px}
    
            div.tab_container .data-table{max-width: 90vw;width: fit-content;}
            div.tab_container .data-table td{border:1px solid #ccc;padding:5px}
            div.tab_container .data-table th{border:1px solid #ccc;background-color: #ddd;padding:5px}
            </style>
            """
            image_result=f'{styles}<div class="tab_container">{image_result}</div>'
        # image_result = json.dumps(objs, indent=4)
        # image_result = re.sub(r"\},", "\n", image_result)
        # image_result = re.sub(r",", "", image_result)
        #
        # image_result = re.sub(r"[\"{}\,]", "", image_result)
        # image_result = re.sub(r'e-\d+', "0.00", image_result)
        #
        # image_result = re.sub(r'-?\d+\.\d+', fmt, image_result)
    except Exception as e:
        image_result = str(e)
    return  Markup(image_result)