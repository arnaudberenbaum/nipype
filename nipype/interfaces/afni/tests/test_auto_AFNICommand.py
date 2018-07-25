# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..base import AFNICommand


def test_AFNICommand_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr='-prefix %s',
            name_source=['in_file'],
            name_template='%s_afni',
        ),
        outputtype=dict(),
    )
    inputs = AFNICommand.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
