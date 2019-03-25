# -*- coding: utf-8 -*-
"""measurement_table.py

This is a dirty script that converts the dictionary of data collected through evaluation.py
to a LaTeX table usable in documentation. Heads up for measurements variable as it covers more data than the
documentation output."""

measurements = {  # Measured using evaluate.py on pretrained HMM model of {1,..,4}-grams
    "Croatian": {
        "training_sentences": 802610,
        1: {"accuracy": 0.9771251284847765, "correct": 3519208, "incorrect": 82386, "word_accuracy": 0.8565050903336895,
            "words_correct": 466588, "words_incorrect": 78170, "diaword_accuracy": 0.0, "diawords_correct": 0,
            "diawords_incorrect": 78170, "alphaword_accuracy": 0.8498102694653922, "alphawords_correct": 442305,
            "alphawords_incorrect": 78170},
        2: {"accuracy": 0.9798836293041359, "correct": 3529143, "incorrect": 72451, "word_accuracy": 0.8736466467679226,
            "words_correct": 475926, "words_incorrect": 68832, "diaword_accuracy": 0.20556479467826533,
            "diawords_correct": 16069, "diawords_incorrect": 62101, "alphaword_accuracy": 0.8677515730822806,
            "alphawords_correct": 451643, "alphawords_incorrect": 68832},
        3: {"accuracy": 0.98455878147287, "correct": 3545981, "incorrect": 55613, "word_accuracy": 0.9025640743229103,
            "words_correct": 491679, "words_incorrect": 53079, "diaword_accuracy": 0.49107074325188693,
            "diawords_correct": 38387, "diawords_incorrect": 39783, "alphaword_accuracy": 0.8980181564916663,
            "alphawords_correct": 467396, "alphawords_incorrect": 53079},
        4: {"accuracy": 0.9886744591422576, "correct": 3560804, "incorrect": 40790, "word_accuracy": 0.9287077931852309,
            "words_correct": 505921, "words_incorrect": 38837, "diaword_accuracy": 0.6183446334911091,
            "diawords_correct": 48336, "diawords_incorrect": 29834, "alphaword_accuracy": 0.9253816225563187,
            "alphawords_correct": 481638, "alphawords_incorrect": 38837}
    },
    "Czech": {
        "training_sentences": 952909,
        1: {"accuracy": 0.8920746971481639, "correct": 3089252, "incorrect": 373745, "word_accuracy": 0.522049677591667,
            "words_correct": 273648, "words_incorrect": 250532, "diaword_accuracy": 0.0, "diawords_correct": 0,
            "diawords_incorrect": 250532, "alphaword_accuracy": 0.49847560060135204, "alphawords_correct": 249009,
            "alphawords_incorrect": 250532},
        2: {"accuracy": 0.904277422128867, "correct": 3131510, "incorrect": 331487, "word_accuracy": 0.5493093975351978,
            "words_correct": 287937, "words_incorrect": 236243, "diaword_accuracy": 0.14081235131639872,
            "diawords_correct": 35278, "diawords_incorrect": 215254, "alphaword_accuracy": 0.5270798593108473,
            "alphawords_correct": 263298, "alphawords_incorrect": 236243},
        3: {"accuracy": 0.924400454288583, "correct": 3201196, "incorrect": 261801, "word_accuracy": 0.6279617688580259,
            "words_correct": 329165, "words_incorrect": 195015, "diaword_accuracy": 0.32120846837928885,
            "diawords_correct": 80473, "diawords_incorrect": 170059, "alphaword_accuracy": 0.6096116234703458,
            "alphawords_correct": 304526, "alphawords_incorrect": 195015},
        4: {"accuracy": 0.9402537744040783, "correct": 3256096, "incorrect": 206901,
            "word_accuracy": 0.6891220573085581, "words_correct": 361224, "words_incorrect": 162956,
            "diaword_accuracy": 0.4327511056471828, "diawords_correct": 108418, "diawords_incorrect": 142114,
            "alphaword_accuracy": 0.6737885378777718, "alphawords_correct": 336585, "alphawords_incorrect": 162956}},
    "Slovak": {
        "training_sentences": 613727,
        1: {"accuracy": 0.9216046105023353, "correct": 2964485, "incorrect": 252171,
            "word_accuracy": 0.5886499485000241, "words_correct": 281752, "words_incorrect": 196889,
            "diaword_accuracy": 0.0, "diawords_correct": 0, "diawords_incorrect": 196889,
            "alphaword_accuracy": 0.5642708709094169, "alphawords_correct": 254972, "alphawords_incorrect": 196889},
        2: {"accuracy": 0.9253252446018474, "correct": 2976453, "incorrect": 240203,
            "word_accuracy": 0.6140071577654234, "words_correct": 293889, "words_incorrect": 184752,
            "diaword_accuracy": 0.12275444539816852, "diawords_correct": 24169, "diawords_incorrect": 172720,
            "alphaword_accuracy": 0.5911309008743839, "alphawords_correct": 267109, "alphawords_incorrect": 184752},
        3: {"accuracy": 0.9384932675424416, "correct": 3018810, "incorrect": 197846,
            "word_accuracy": 0.6693868682373637, "words_correct": 320396, "words_incorrect": 158245,
            "diaword_accuracy": 0.2736567304420257, "diawords_correct": 53880, "diawords_incorrect": 143009,
            "alphaword_accuracy": 0.6497927459993228, "alphawords_correct": 293616, "alphawords_incorrect": 158245},
        4: {"accuracy": 0.9506714426410533, "correct": 3057983, "incorrect": 158673,
            "word_accuracy": 0.7265528861923655, "words_correct": 347758, "words_incorrect": 130883,
            "diaword_accuracy": 0.4200996500566309, "diawords_correct": 82713, "diawords_incorrect": 114176,
            "alphaword_accuracy": 0.7103467659302307, "alphawords_correct": 320978, "alphawords_incorrect": 130883}
    },
    "Irish": {
        "training_sentences": 50825,
        1: {"accuracy": 0.9424253729918602, "correct": 3455593, "incorrect": 211109,
            "word_accuracy": 0.7029482665651664, "words_correct": 443237, "words_incorrect": 187303,
            "diaword_accuracy": 0.0, "diawords_correct": 0, "diawords_incorrect": 187303,
            "alphaword_accuracy": 0.6952143066358577, "alphawords_correct": 427237, "alphawords_incorrect": 187303},
        2: {"accuracy": 0.9475430509487818, "correct": 3474358, "incorrect": 192344,
            "word_accuracy": 0.7323437053953754, "words_correct": 461772, "words_incorrect": 168768,
            "diaword_accuracy": 0.2101247710928282, "diawords_correct": 39357, "diawords_incorrect": 147946,
            "alphaword_accuracy": 0.7253750772935854, "alphawords_correct": 445772, "alphawords_incorrect": 168768},
        3: {"accuracy": 0.9567949617940046, "correct": 3508282, "incorrect": 158420, "word_accuracy": 0.778226599422717,
            "words_correct": 490703, "words_incorrect": 139837, "diaword_accuracy": 0.4029139949707159,
            "diawords_correct": 75467, "diawords_incorrect": 111836, "alphaword_accuracy": 0.7724525661470368,
            "alphawords_correct": 474703, "alphawords_incorrect": 139837},
        4: {"accuracy": 0.9613922811289273, "correct": 3525139, "incorrect": 141563,
            "word_accuracy": 0.7999207028895867, "words_correct": 504382, "words_incorrect": 126158,
            "diaword_accuracy": 0.4465865469319765, "diawords_correct": 83647, "diawords_incorrect": 103656,
            "alphaword_accuracy": 0.7947114915221141, "alphawords_correct": 488382, "alphawords_incorrect": 126158}},
    "Hungarian": {
        "training_sentences": 1294605,
        1: {"accuracy": 0.9058813212263882, "correct": 3429500, "incorrect": 356316, "word_accuracy": 0.526094626855209,
            "words_correct": 270178, "words_incorrect": 243376, "diaword_accuracy": 0.0, "diawords_correct": 0,
            "diawords_incorrect": 243376, "alphaword_accuracy": 0.5072801775100011, "alphawords_correct": 250568,
            "alphawords_incorrect": 243376},
        2: {"accuracy": 0.9060678067819461, "correct": 3430206, "incorrect": 355610,
            "word_accuracy": 0.5204944368070349, "words_correct": 267302, "words_incorrect": 246252,
            "diaword_accuracy": 0.07922720399710735, "diawords_correct": 19282, "diawords_incorrect": 224094,
            "alphaword_accuracy": 0.5014576551187989, "alphawords_correct": 247692, "alphawords_incorrect": 246252},
        3: {"accuracy": 0.9241508303625955, "correct": 3498665, "incorrect": 287151,
            "word_accuracy": 0.5868321539701764, "words_correct": 301370, "words_incorrect": 212184,
            "diaword_accuracy": 0.2669573006376964, "diawords_correct": 64971, "diawords_incorrect": 178405,
            "alphaword_accuracy": 0.5704290364899665, "alphawords_correct": 281760, "alphawords_incorrect": 212184},
        4: {"accuracy": 0.9387299858207583, "correct": 3553859, "incorrect": 231957,
            "word_accuracy": 0.6487399572391608, "words_correct": 333163, "words_incorrect": 180391,
            "diaword_accuracy": 0.3804113799224246, "diawords_correct": 92583, "diawords_incorrect": 150793,
            "alphaword_accuracy": 0.6347946325899292, "alphawords_correct": 313553, "alphawords_incorrect": 180391}},
    "Polish": {
        "training_sentences": 1069841,
        1: {"accuracy": 0.9464899238731393, "correct": 3473300, "incorrect": 196364,
            "word_accuracy": 0.6842926583216262, "words_correct": 347297, "words_incorrect": 160230,
            "diaword_accuracy": 0.0, "diawords_correct": 0, "diawords_incorrect": 160230,
            "alphaword_accuracy": 0.6687546514512528, "alphawords_correct": 323490, "alphawords_incorrect": 160230},
        2: {"accuracy": 0.9489097639456909, "correct": 3482180, "incorrect": 187484,
            "word_accuracy": 0.7010760018678809, "words_correct": 355815, "words_incorrect": 151712,
            "diaword_accuracy": 0.16392685514572802, "diawords_correct": 26266, "diawords_incorrect": 133964,
            "alphaword_accuracy": 0.6863640122384851, "alphawords_correct": 332008, "alphawords_incorrect": 151712},
        3: {"accuracy": 0.9605236337713753, "correct": 3524799, "incorrect": 144865, "word_accuracy": 0.762188021523978,
            "words_correct": 386831, "words_incorrect": 120696, "diaword_accuracy": 0.3529738500904949,
            "diawords_correct": 56557, "diawords_incorrect": 103673, "alphaword_accuracy": 0.7504837509302903,
            "alphawords_correct": 363024, "alphawords_incorrect": 120696},
        4: {"accuracy": 0.969200722463964, "correct": 3556641, "incorrect": 113023, "word_accuracy": 0.8091943876877487,
            "words_correct": 410688, "words_incorrect": 96839, "diaword_accuracy": 0.4927604069150596,
            "diawords_correct": 78955, "diawords_incorrect": 81275, "alphaword_accuracy": 0.7998036053915488,
            "alphawords_correct": 386881, "alphawords_incorrect": 96839}
    },
    "Romanian": {
        "training_sentences": 837647,
        1: {"accuracy": 0.94975410129696, "correct": 3897334, "incorrect": 206185, "word_accuracy": 0.7232841335369187,
            "words_correct": 460434, "words_incorrect": 176154, "diaword_accuracy": 0.023425588978288208,
            "diawords_correct": 4210, "diawords_incorrect": 175508, "alphaword_accuracy": 0.7093715043704649,
            "alphawords_correct": 429960, "alphawords_incorrect": 176154},
        2: {"accuracy": 0.9528982319808925, "correct": 3910236, "incorrect": 193283, "word_accuracy": 0.74150785123188,
            "words_correct": 472035, "words_incorrect": 164553, "diaword_accuracy": 0.16358962374386538,
            "diawords_correct": 29400, "diawords_incorrect": 150318, "alphaword_accuracy": 0.728511468139657,
            "alphawords_correct": 441561, "alphawords_incorrect": 164553},
        3: {"accuracy": 0.957873717655505, "correct": 3930653, "incorrect": 172866, "word_accuracy": 0.7682378555674942,
            "words_correct": 489051, "words_incorrect": 147537, "diaword_accuracy": 0.3102805506404478,
            "diawords_correct": 55763, "diawords_incorrect": 123955, "alphaword_accuracy": 0.7565853948267157,
            "alphawords_correct": 458577, "alphawords_incorrect": 147537},
        4: {"accuracy": 0.9636723992261276, "correct": 3954448, "incorrect": 149071,
            "word_accuracy": 0.7970869699083237, "words_correct": 507416, "words_incorrect": 129172,
            "diaword_accuracy": 0.43134243648382464, "diawords_correct": 77520, "diawords_incorrect": 102198,
            "alphaword_accuracy": 0.7868849754336643, "alphawords_correct": 476942, "alphawords_incorrect": 129172}
    },
    "French": {
        "training_sentences": 1818618,
        1: {"accuracy": 0.9700007188776134, "correct": 4304352, "incorrect": 133121,
            "word_accuracy": 0.8341954430548719, "words_correct": 599925, "words_incorrect": 119241,
            "diaword_accuracy": 0.0, "diawords_correct": 0, "diawords_incorrect": 119241,
            "alphaword_accuracy": 0.8262428761488143, "alphawords_correct": 567010, "alphawords_incorrect": 119241},
        2: {"accuracy": 0.9700007188776134, "correct": 4304352, "incorrect": 133121,
            "word_accuracy": 0.8341954430548719, "words_correct": 599925, "words_incorrect": 119241,
            "diaword_accuracy": 0.0, "diawords_correct": 0, "diawords_incorrect": 119241,
            "alphaword_accuracy": 0.8262428761488143, "alphawords_correct": 567010, "alphawords_incorrect": 119241},
        3: {"accuracy": 0.9713282762509203, "correct": 4310243, "incorrect": 127230,
            "word_accuracy": 0.8401871056195649, "words_correct": 604234, "words_incorrect": 114932,
            "diaword_accuracy": 0.09328167324997275, "diawords_correct": 11123, "diawords_incorrect": 108118,
            "alphaword_accuracy": 0.832521919822339, "alphawords_correct": 571319, "alphawords_incorrect": 114932},
        4: {"accuracy": 0.9753717938114779, "correct": 4328186, "incorrect": 109287,
            "word_accuracy": 0.8609208444225672, "words_correct": 619145, "words_incorrect": 100021,
            "diaword_accuracy": 0.2736726461535881, "diawords_correct": 32633, "diawords_incorrect": 86608,
            "alphaword_accuracy": 0.8542501213112986, "alphawords_correct": 586230, "alphawords_incorrect": 100021}},
    "Spanish": {
        "training_sentences": 1735516,
        1: {"accuracy": 0.9808013495827422, "correct": 4787209, "incorrect": 93707, "word_accuracy": 0.8824002535407957,
            "words_correct": 698846, "words_incorrect": 93137, "diaword_accuracy": 0.0, "diawords_correct": 0,
            "diawords_incorrect": 93137, "alphaword_accuracy": 0.879536912248208, "alphawords_correct": 680021,
            "alphawords_incorrect": 93137},
        2: {"accuracy": 0.9808017593418941, "correct": 4787211, "incorrect": 93705, "word_accuracy": 0.8824027788475257,
            "words_correct": 698848, "words_incorrect": 93135, "diaword_accuracy": 2.1473742980770263e-05,
            "diawords_correct": 2, "diawords_incorrect": 93135, "alphaword_accuracy": 0.879539499041593,
            "alphawords_correct": 680023, "alphawords_incorrect": 93135},
        3: {"accuracy": 0.9824295275722835, "correct": 4795156, "incorrect": 85760, "word_accuracy": 0.8929042668845164,
            "words_correct": 707165, "words_incorrect": 84818, "diaword_accuracy": 0.21785112253991432,
            "diawords_correct": 20290, "diawords_incorrect": 72847, "alphaword_accuracy": 0.8902966793333316,
            "alphawords_correct": 688340, "alphawords_incorrect": 84818},
        4: {"accuracy": 0.9847979354694898, "correct": 4806716, "incorrect": 74200, "word_accuracy": 0.9092707798020917,
            "words_correct": 720127, "words_incorrect": 71856, "diaword_accuracy": 0.37843177255011434,
            "diawords_correct": 35246, "diawords_incorrect": 57891, "alphaword_accuracy": 0.9070616872618533,
            "alphawords_correct": 701302, "alphawords_incorrect": 71856}},
    "Latvian": {
        "training_sentences": 315807,
        1: {"accuracy": 0.9145115850913708, "correct": 2892944, "incorrect": 270432,
            "word_accuracy": 0.5323272703960142, "words_correct": 232495, "words_incorrect": 204257,
            "diaword_accuracy": 0.0, "diawords_correct": 0, "diawords_incorrect": 204257,
            "alphaword_accuracy": 0.5019907593655902, "alphawords_correct": 205889, "alphawords_incorrect": 204256},
        2: {"accuracy": 0.9147723824167598, "correct": 2893769, "incorrect": 269607,
            "word_accuracy": 0.5381772722277174, "words_correct": 235050, "words_incorrect": 201702,
            "diaword_accuracy": 0.02892924110312009, "diawords_correct": 5909, "diawords_incorrect": 198348,
            "alphaword_accuracy": 0.5082202635653245, "alphawords_correct": 208444, "alphawords_incorrect": 201701},
        3: {"accuracy": 0.9241753114394242, "correct": 2923514, "incorrect": 239862, "word_accuracy": 0.589160438876067,
            "words_correct": 257317, "words_incorrect": 179435, "diaword_accuracy": 0.24009948251467514,
            "diawords_correct": 49042, "diawords_incorrect": 155215, "alphaword_accuracy": 0.5625108193443782,
            "alphawords_correct": 230711, "alphawords_incorrect": 179434},
        4: {"accuracy": 0.9389680518534629, "correct": 2970309, "incorrect": 193067,
            "word_accuracy": 0.6540393632999963, "words_correct": 285653, "words_incorrect": 151099,
            "diaword_accuracy": 0.38025135001493215, "diawords_correct": 77669, "diawords_incorrect": 126588,
            "alphaword_accuracy": 0.63159858098965, "alphawords_correct": 259047, "alphawords_incorrect": 151098}
    },
}
lines = []
line = []

for language, measurement in measurements.items():
    #  Print LaTeX formatted accuracy table
    line.append("\hline\n\\textbf{" + language + "}")
    line.append("{:,}".format((measurement["training_sentences"])))
    dia_percent = '{:.1%}'.format((measurement[1]["diawords_correct"] + measurement[1]["diawords_incorrect"]) / (
            measurement[1]["words_correct"] + measurement[1]["words_incorrect"]))
    line.append(dia_percent.replace("%", "\\%"))
    for i in range(1, 5):
        if not line:
            line += [" ", " ", " "]
        line.append(str(i))
        for accuracy in ["accuracy", "word_accuracy", "diaword_accuracy", "alphaword_accuracy"]:
            line.append('{0:.3g}'.format(measurement[i][accuracy]))
            if i == 4:
                line[-1] = "\\textbf{" + line[-1] + "}"
        lines.append(line)
        line = []

print("\\\\ \\cline{4-8}\n".join([" & ".join(row) for row in lines] + ['\hline']))
