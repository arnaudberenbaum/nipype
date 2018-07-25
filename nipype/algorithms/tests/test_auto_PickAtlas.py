# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..misc import PickAtlas


def test_PickAtlas_inputs():
    input_map = dict(
        atlas=dict(mandatory=True, ),
        dilation_size=dict(usedefault=True, ),
        hemi=dict(usedefault=True, ),
        labels=dict(mandatory=True, ),
        output_file=dict(),
    )
    inputs = PickAtlas.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_PickAtlas_outputs():
    output_map = dict(mask_file=dict(), )
    outputs = PickAtlas.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
