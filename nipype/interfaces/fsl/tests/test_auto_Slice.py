# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Slice


def test_Slice_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            copyfile=False,
            mandatory=True,
            position=0,
        ),
        out_base_name=dict(
            argstr='%s',
            position=1,
        ),
        output_type=dict(),
    )
    inputs = Slice.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Slice_outputs():
    output_map = dict(out_files=dict(), )
    outputs = Slice.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
