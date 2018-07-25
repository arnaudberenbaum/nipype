# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..svm import SVMTest


def test_SVMTest_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        classout=dict(argstr='-classout', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-testvol %s',
            mandatory=True,
        ),
        model=dict(
            argstr='-model %s',
            mandatory=True,
        ),
        multiclass=dict(argstr='-multiclass %s', ),
        nodetrend=dict(argstr='-nodetrend', ),
        nopredcensord=dict(argstr='-nopredcensord', ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        options=dict(argstr='%s', ),
        out_file=dict(
            argstr='-predictions %s',
            name_template='%s_predictions',
        ),
        outputtype=dict(),
        testlabels=dict(argstr='-testlabels %s', ),
    )
    inputs = SVMTest.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SVMTest_outputs():
    output_map = dict(out_file=dict(), )
    outputs = SVMTest.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
