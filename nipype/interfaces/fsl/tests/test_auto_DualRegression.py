# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..model import DualRegression


def test_DualRegression_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        con_file=dict(
            argstr='%s',
            position=4,
        ),
        des_norm=dict(
            argstr='%i',
            position=2,
            usedefault=True,
        ),
        design_file=dict(
            argstr='%s',
            position=3,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        group_IC_maps_4D=dict(
            argstr='%s',
            mandatory=True,
            position=1,
        ),
        in_files=dict(
            argstr='%s',
            mandatory=True,
            position=-1,
            sep=' ',
        ),
        n_perm=dict(
            argstr='%i',
            mandatory=True,
            position=5,
        ),
        one_sample_group_mean=dict(
            argstr='-1',
            position=3,
        ),
        out_dir=dict(
            argstr='%s',
            genfile=True,
            position=6,
            usedefault=True,
        ),
        output_type=dict(),
    )
    inputs = DualRegression.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DualRegression_outputs():
    output_map = dict(out_dir=dict(), )
    outputs = DualRegression.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
