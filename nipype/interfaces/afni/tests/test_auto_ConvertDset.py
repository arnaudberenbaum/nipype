# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import ConvertDset


def test_ConvertDset_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-input %s',
            mandatory=True,
            position=-2,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr='-prefix %s',
            mandatory=True,
            position=-1,
        ),
        out_type=dict(
            argstr='-o_%s',
            mandatory=True,
            position=0,
        ),
        outputtype=dict(),
    )
    inputs = ConvertDset.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ConvertDset_outputs():
    output_map = dict(out_file=dict(), )
    outputs = ConvertDset.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
