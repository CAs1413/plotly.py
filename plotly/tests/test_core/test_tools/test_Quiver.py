import plotly
from plotly.graph_objs import *
import plotly.tools as tls
from nose.tools import raises
import numpy as np


@raises(Exception)
def unequal_xy_length():
    data = tls.Quiver(x=[1, 2], y=[1], u=[1, 2], v=[1, 2])


@raises(Exception)
def unequal_uv_length():
    data = tls.Quiver(x=[1, 2], y=[1, 3], u=[1], v=[1, 2])


@raises(Exception)
def test_wrong_kwarg():
    data = tls.Quiver(stuff='not gonna work')


def test_one_arrow():
    nan = np.nan
    trace1 = Scatter(
            x=[0., 1., nan],
            y=[0., 1., nan],
            mode='lines',
            name='Barb',
            line=Line(color='rgb(114, 132, 314)', width=1)
            )
    trace2 = Scatter(
            x=[0.82069826, 1., 0.61548617, nan],
            y=[0.61548617,  1.,  0.82069826, nan],
            mode='lines',
            name='Arrow',
            line=Line(color='rgb(114, 132, 314)', width=1)
            )
    expected = Data([trace1, trace2])

    data = tls.Quiver(x=[0], y=[0], u=[1], v=[1], scale=1)

    np.testing.assert_almost_equal(data[0]['y'], expected[0]['y'])
    np.testing.assert_almost_equal(data[0]['x'], expected[0]['x'])
    np.testing.assert_almost_equal(data[1]['y'], expected[1]['y'])
    np.testing.assert_almost_equal(data[1]['x'], expected[1]['x'])
    assert data[0].keys() == expected[0].keys()


def test_complicated():
    nan = np.nan
    trace1 = Scatter(
            x=[0.0, 0.5, nan, 0.0, 0.5, nan, 0.0, 0.5, nan, 0.0, 0.5, nan, 0.0, 0.5, nan, 0.0, 0.5, nan, 0.0, 0.5, nan, 0.5, 0.9387912809451864, nan, 0.5, 0.9387912809451864, nan, 0.5, 0.9387912809451864, nan, 0.5, 0.9387912809451864, nan, 0.5, 0.9387912809451864, nan, 0.5, 0.9387912809451864, nan, 0.5, 0.9387912809451864, nan, 1.0, 1.2701511529340699, nan, 1.0, 1.2701511529340699, nan, 1.0, 1.2701511529340699, nan, 1.0, 1.2701511529340699, nan, 1.0, 1.2701511529340699, nan, 1.0, 1.2701511529340699, nan, 1.0, 1.2701511529340699, nan, 1.5, 1.5353686008338514, nan, 1.5, 1.5353686008338514, nan, 1.5, 1.5353686008338514, nan, 1.5, 1.5353686008338514, nan, 1.5, 1.5353686008338514, nan, 1.5, 1.5353686008338514, nan, 1.5, 1.5353686008338514, nan, 2.0, 1.7919265817264287, nan, 2.0, 1.7919265817264287, nan, 2.0, 1.7919265817264287, nan, 2.0, 1.7919265817264287, nan, 2.0, 1.7919265817264287, nan, 2.0, 1.7919265817264287, nan, 2.0, 1.7919265817264287, nan, 2.5, 2.099428192226533, nan, 2.5, 2.099428192226533, nan, 2.5, 2.099428192226533, nan, 2.5, 2.099428192226533, nan, 2.5, 2.099428192226533, nan, 2.5, 2.099428192226533, nan, 2.5, 2.099428192226533, nan, 3.0, 2.5050037516997774, nan, 3.0, 2.5050037516997774, nan, 3.0, 2.5050037516997774, nan, 3.0, 2.5050037516997774, nan, 3.0, 2.5050037516997774, nan, 3.0, 2.5050037516997774, nan, 3.0, 2.5050037516997774, nan],
            y=[0.0, 0.0, nan, 0.5, 0.7397127693021015, nan, 1.0, 1.4207354924039484, nan, 1.5, 1.9987474933020273, nan, 2.0, 2.454648713412841, nan, 2.5, 2.799236072051978, nan, 3.0, 3.0705600040299337, nan, 0.0, 0.0, nan, 0.5, 0.7397127693021015, nan, 1.0, 1.4207354924039484, nan, 1.5, 1.9987474933020273, nan, 2.0, 2.454648713412841, nan, 2.5, 2.799236072051978, nan, 3.0, 3.0705600040299337, nan, 0.0, 0.0, nan, 0.5, 0.7397127693021015, nan, 1.0, 1.4207354924039484, nan, 1.5, 1.9987474933020273, nan, 2.0, 2.454648713412841, nan, 2.5, 2.799236072051978, nan, 3.0, 3.0705600040299337, nan, 0.0, 0.0, nan, 0.5, 0.7397127693021015, nan, 1.0, 1.4207354924039484, nan, 1.5, 1.9987474933020273, nan, 2.0, 2.454648713412841, nan, 2.5, 2.799236072051978, nan, 3.0, 3.0705600040299337, nan, 0.0, 0.0, nan, 0.5, 0.7397127693021015, nan, 1.0, 1.4207354924039484, nan, 1.5, 1.9987474933020273, nan, 2.0, 2.454648713412841, nan, 2.5, 2.799236072051978, nan, 3.0, 3.0705600040299337, nan, 0.0, 0.0, nan, 0.5, 0.7397127693021015, nan, 1.0, 1.4207354924039484, nan, 1.5, 1.9987474933020273, nan, 2.0, 2.454648713412841, nan, 2.5, 2.799236072051978, nan, 3.0, 3.0705600040299337, nan, 0.0, 0.0, nan, 0.5, 0.7397127693021015, nan, 1.0, 1.4207354924039484, nan, 1.5, 1.9987474933020273, nan, 2.0, 2.454648713412841, nan, 2.5, 2.799236072051978, nan, 3.0, 3.0705600040299337, nan],
            mode='lines',
            name='Barb',
            line=Line(color='rgb(114, 132, 314)', width=2)
            )
    trace2 = Scatter(
            x=[0.38451505843608913, 0.5, 0.38451505843608913, nan, 0.40744858477065643, 0.5, 0.3615815321015219, nan, 0.4247671840238289, 0.5, 0.3442629328483494, nan, 0.43223065909116526, 0.5, 0.33679945778101306, nan, 0.42801169097838865, 0.5, 0.3410184258937896, nan, 0.4131432302211637, 0.5, 0.3558868866510146, nan, 0.39126559456855653, 0.5, 0.37776452230362173, nan, 0.8374437100677695, 0.9387912809451864, 0.8374437100677695, nan, 0.8603772364023368, 0.9387912809451864, 0.8145101837332023, nan, 0.8776958356555092, 0.9387912809451864, 0.7971915844800297, nan, 0.8851593107228456, 0.9387912809451864, 0.7897281094126934, nan, 0.880940342610069, 0.9387912809451864, 0.79394707752547, nan, 0.8660718818528441, 0.9387912809451864, 0.8088155382826949, nan, 0.8441942462002369, 0.9387912809451864, 0.8306931739353021, nan, 1.2077543727140414, 1.2701511529340699, 1.2077543727140414, nan, 1.2306878990486088, 1.2701511529340699, 1.1848208463794743, nan, 1.2480064983017813, 1.2701511529340699, 1.1675022471263017, nan, 1.2554699733691175, 1.2701511529340699, 1.1600387720589653, nan, 1.251251005256341, 1.2701511529340699, 1.164257740171742, nan, 1.236382544499116, 1.2701511529340699, 1.179126200928967, nan, 1.214504908846509, 1.2701511529340699, 1.201003836581574, nan, 1.5271995192328622, 1.5353686008338514, 1.5271995192328622, nan, 1.5501330455674294, 1.5353686008338514, 1.5042659928982949, nan, 1.567451644820602, 1.5353686008338514, 1.4869473936451223, nan, 1.5749151198879383, 1.5353686008338514, 1.4794839185777862, nan, 1.5706961517751616, 1.5353686008338514, 1.4837028866905626, nan, 1.5558276910179367, 1.5353686008338514, 1.4985713474477875, nan, 1.5339500553653296, 1.5353686008338514, 1.5204489831003947, nan, 1.8399852748270817, 1.7919265817264287, 1.8399852748270817, nan, 1.862918801161649, 1.7919265817264287, 1.8170517484925146, nan, 1.8802374004148217, 1.7919265817264287, 1.799733149239342, nan, 1.887700875482158, 1.7919265817264287, 1.7922696741720057, nan, 1.8834819073693814, 1.7919265817264287, 1.7964886422847823, nan, 1.8686134466121564, 1.7919265817264287, 1.8113571030420073, nan, 1.8467358109595493, 1.7919265817264287, 1.8332347386946144, nan, 2.1919482158522707, 2.099428192226533, 2.1919482158522707, nan, 2.2148817421868383, 2.099428192226533, 2.1690146895177036, nan, 2.2322003414400107, 2.099428192226533, 2.1516960902645312, nan, 2.2396638165073472, 2.099428192226533, 2.1442326151971947, nan, 2.2354448483945704, 2.099428192226533, 2.1484515833099715, nan, 2.2205763876373457, 2.099428192226533, 2.1633200440671962, nan, 2.1986987519847383, 2.099428192226533, 2.1851976797198036, nan, 2.61933297731839, 2.5050037516997774, 2.61933297731839, nan, 2.6422665036529573, 2.5050037516997774, 2.5963994509838226, nan, 2.6595851029061297, 2.5050037516997774, 2.5790808517306503, nan, 2.6670485779734663, 2.5050037516997774, 2.571617376663314, nan, 2.6628296098606894, 2.5050037516997774, 2.5758363447760906, nan, 2.6479611491034647, 2.5050037516997774, 2.5907048055333153, nan, 2.6260835134508573, 2.5050037516997774, 2.6125824411859226, nan],
            y=[-0.04783542904563622, 0.0, 0.04783542904563622, nan, 0.6365109099465124, 0.7397127693021015, 0.7321817680377849, nan, 1.2757228358500456, 1.4207354924039484, 1.371393693941318, nan, 1.835716414018128, 1.9987474933020273, 1.9313872721094003, nan, 2.3018031241660264, 2.454648713412841, 2.397473982257299, nan, 2.682286122416868, 2.799236072051978, 2.7779569805081405, nan, 3.006427339100005, 3.0705600040299337, 3.1020981971912773, nan, -0.041979538370994586, 0.0, 0.041979538370994586, nan, 0.642366800621154, 0.7397127693021015, 0.7263258773631432, nan, 1.2815787265246874, 1.4207354924039484, 1.3655378032666765, nan, 1.8415723046927694, 1.9987474933020273, 1.9255313814347585, nan, 2.307659014840668, 2.454648713412841, 2.3916180915826573, nan, 2.6881420130915097, 2.799236072051978, 2.772101089833499, nan, 3.0122832297746465, 3.0705600040299337, 3.096242306516636, nan, -0.02584559261554904, 0.0, 0.02584559261554904, nan, 0.6585007463765996, 0.7397127693021015, 0.7101919316076977, nan, 1.2977126722801329, 1.4207354924039484, 1.349403857511231, nan, 1.857706250448215, 1.9987474933020273, 1.909397435679313, nan, 2.3237929605961134, 2.454648713412841, 2.375484145827212, nan, 2.704275958846955, 2.799236072051978, 2.7559671440780535, nan, 3.0284171755300924, 3.0705600040299337, 3.0801083607611903, nan, -0.003383744391262258, 0.0, 0.003383744391262258, nan, 0.6809625946008864, 0.7397127693021015, 0.6877300833834109, nan, 1.3201745205044197, 1.4207354924039484, 1.3269420092869442, nan, 1.8801680986725018, 1.9987474933020273, 1.8869355874550262, nan, 2.3462548088204005, 2.454648713412841, 2.3530222976029247, nan, 2.7267378070712422, 2.799236072051978, 2.7335052958537664, nan, 3.050879023754379, 3.0705600040299337, 3.0576465125369037, nan, 0.019906562472216813, 0.0, -0.019906562472216813, nan, 0.7042529014643655, 0.7397127693021015, 0.6644397765199318, nan, 1.3434648273678986, 1.4207354924039484, 1.303651702423465, nan, 1.903458405535981, 1.9987474933020273, 1.863645280591547, nan, 2.3695451156838794, 2.454648713412841, 2.329731990739446, nan, 2.750028113934721, 2.799236072051978, 2.7102149889902876, nan, 3.074169330617858, 3.0705600040299337, 3.0343562056734243, nan, 0.03832304857685983, 0.0, -0.03832304857685983, nan, 0.7226693875690084, 0.7397127693021015, 0.6460232904152888, nan, 1.3618813134725418, 1.4207354924039484, 1.285235216318822, nan, 1.9218748916406239, 1.9987474933020273, 1.8452287944869041, nan, 2.3879616017885223, 2.454648713412841, 2.311315504634803, nan, 2.768444600039364, 2.799236072051978, 2.6917985028856446, nan, 3.092585816722501, 3.0705600040299337, 3.0159397195687814, nan, 0.04735671582684286, 0.0, -0.04735671582684286, nan, 0.7317030548189914, 0.7397127693021015, 0.6369896231653058, nan, 1.3709149807225247, 1.4207354924039484, 1.276201549068839, nan, 1.9309085588906068, 1.9987474933020273, 1.8361951272369212, nan, 2.3969952690385052, 2.454648713412841, 2.30228183738482, nan, 2.7774782672893474, 2.799236072051978, 2.6827648356356617, nan, 3.101619483972484, 3.0705600040299337, 3.0069060523187985, nan],
            mode='lines',
            name='Arrow',
            line=Line(color='rgb(114, 132, 314)', width=3)
            )
    expected = Data([trace1, trace2])

    x, y = np.meshgrid(np.arange(0, np.pi, .5), np.arange(0, np.pi, .5))
    u = np.cos(x)
    v = np.sin(y)
    data = tls.Quiver(x, y, u, v, scale=.5, angle=np.pi/8,
                      arrow_scale=.25, barb_width=2
                      arrow_width=3)

    # np.testing.assert_almost_equal(data[0]['y'], expected[0]['y'])
    # np.testing.assert_almost_equal(data[0]['x'], expected[0]['x'])
    np.testing.assert_almost_equal(data[1]['y'], expected[1]['y'])
    np.testing.assert_almost_equal(data[1]['x'], expected[1]['x'])
    assert data[0].keys() == expected[0].keys()
