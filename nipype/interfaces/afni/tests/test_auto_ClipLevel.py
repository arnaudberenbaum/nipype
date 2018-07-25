# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import ClipLevel


def test_ClipLevel_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        doall=dict(
            argstr='-doall',
            position=3,
            xor='grad',
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        grad=dict(
            argstr='-grad %s',
            position=3,
            xor='doall',
        ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=-1,
        ),
        mfrac=dict(
            argstr='-mfrac %s',
            position=2,
        ),
    )
    inputs = ClipLevel.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ClipLevel_outputs():
    output_map = dict(clip_val=dict(), )
    outputs = ClipLevel.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
