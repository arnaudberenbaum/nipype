# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import RobustFOV


def test_RobustFOV_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        brainsize=dict(argstr='-b %d', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-i %s',
            mandatory=True,
            position=0,
        ),
        out_roi=dict(
            argstr='-r %s',
            hash_files=False,
            name_source=['in_file'],
            name_template='%s_ROI',
        ),
        out_transform=dict(
            argstr='-m %s',
            hash_files=False,
            name_source=['in_file'],
            name_template='%s_to_ROI',
        ),
        output_type=dict(),
    )
    inputs = RobustFOV.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_RobustFOV_outputs():
    output_map = dict(
        out_roi=dict(),
        out_transform=dict(),
    )
    outputs = RobustFOV.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
