from flask import Flask, render_template, request
import teadata, tea, random

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    td = teadata.TeaData()

    return render_template('index.html', td=td)

@app.route("/tea", methods=['GET', 'POST'])
def tea_rec_page():

    hasCaffeine = ""
    region = ""
    feeling = ""
    condition = ""


    if request.method == "GET":
        hasCaffeine = request.args.get("caffeine") == 'on'
        region = request.args.get("region") or 'Any'
        feeling = request.args.get("feeling") or 'Any'
        condition = request.args.get("condition") or 'Any'
        #print(hasCaffeine + region + feeling + condition)

    td = teadata.TeaData()
    
    full_tea_list = teadata.import_tea()
    full_tea_list.__delitem__(0)

    normal_tea_list = []
    rare_tea_list = []

    for tea in full_tea_list:
        if tea.rare == "niche":
            rare_tea_list.append(tea)
        else:
            normal_tea_list.append(tea)

    # filter by feeling
    tmp_list = []
    for tea in normal_tea_list:
        if tea.feeling == feeling or feeling == 'any':
            tmp_list.append(tea)
    normal_tea_list = tmp_list

    tmp_list = []
    for tea in rare_tea_list:
        if tea.feeling == feeling or feeling == 'any':
            tmp_list.append(tea)
    rare_tea_list = tmp_list

    # filter by feeling
    tmp_list = []
    for tea in normal_tea_list:
        if tea.caffeine == hasCaffeine:
            tmp_list.append(tea)
    normal_tea_list = tmp_list

    tmp_list = []
    for tea in rare_tea_list:
        if tea.caffeine == hasCaffeine:
            tmp_list.append(tea)
    rare_tea_list = tmp_list
    
    #filter by region
    tmp_list = []
    for tea in normal_tea_list:
        if tea.regions.count(region) > 0 or region == 'any':
            tmp_list.append(tea)
    normal_tea_list = tmp_list

    tmp_list = []
    for tea in rare_tea_list:
        if tea.regions.count(region) > 0 or region == 'any':
            tmp_list.append(tea)
    rare_tea_list = tmp_list

    #filter by condition
    tmp_list = []
    for tea in normal_tea_list:
        if tea.diseases.count(condition) > 0 or condition == 'any':
            tmp_list.append(tea)
    normal_tea_list = tmp_list

    tmp_list = []
    for tea in rare_tea_list:
        if tea.diseases.count(condition) > 0 or condition == 'any':
            tmp_list.append(tea)
    rare_tea_list = tmp_list

    if len(normal_tea_list) == 0:
        normal_tea_list = [teadata.blank_tea]
    
    if len(rare_tea_list) == 0:
        rare_tea_list = [teadata.blank_tea]

    tea1 = random.choice(normal_tea_list)
    tea2 = random.choice(rare_tea_list)

    return render_template('tearec.html', td=td, tea1=tea1, tea2=tea2)
