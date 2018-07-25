# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import ImageStats


def test_ImageStats_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_files=dict(
            argstr='-images %s',
            mandatory=True,
            position=-1,
        ),
        out_type=dict(
            argstr='-outputdatatype %s',
            usedefault=True,
        ),
        output_root=dict(
            argstr='-outputroot %s',
            mandatory=True,
        ),
        stat=dict(
            argstr='-stat %s',
            mandatory=True,
            units='NA',
        ),
    )
    inputs = ImageStats.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ImageStats_outputs():
    output_map = dict(out_file=dict(), )
    outputs = ImageStats.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
