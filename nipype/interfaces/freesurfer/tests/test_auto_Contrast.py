# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Contrast


def test_Contrast_inputs():
    input_map = dict(
        annotation=dict(mandatory=True, ),
        args=dict(argstr='%s', ),
        copy_inputs=dict(),
        cortex=dict(mandatory=True, ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        hemisphere=dict(
            argstr='--%s-only',
            mandatory=True,
        ),
        orig=dict(mandatory=True, ),
        rawavg=dict(mandatory=True, ),
        subject_id=dict(
            argstr='--s %s',
            mandatory=True,
            usedefault=True,
        ),
        subjects_dir=dict(),
        thickness=dict(mandatory=True, ),
        white=dict(mandatory=True, ),
    )
    inputs = Contrast.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Contrast_outputs():
    output_map = dict(
        out_contrast=dict(),
        out_log=dict(),
        out_stats=dict(),
    )
    outputs = Contrast.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
