# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import DiffeoTask


def test_DiffeoTask_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fixed_file=dict(
            argstr='%s',
            position=0,
        ),
        ftol=dict(
            argstr='%g',
            mandatory=True,
            position=5,
            usedefault=True,
        ),
        legacy=dict(
            argstr='%d',
            mandatory=True,
            position=3,
            usedefault=True,
        ),
        mask_file=dict(
            argstr='%s',
            position=2,
        ),
        moving_file=dict(
            argstr='%s',
            copyfile=False,
            position=1,
        ),
        n_iters=dict(
            argstr='%d',
            mandatory=True,
            position=4,
            usedefault=True,
        ),
    )
    inputs = DiffeoTask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DiffeoTask_outputs():
    output_map = dict(
        out_file=dict(),
        out_file_xfm=dict(),
    )
    outputs = DiffeoTask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
