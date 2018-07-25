# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..convert import MRTrix2TrackVis


def test_MRTrix2TrackVis_inputs():
    input_map = dict(
        image_file=dict(),
        in_file=dict(mandatory=True, ),
        matrix_file=dict(),
        out_filename=dict(
            genfile=True,
            usedefault=True,
        ),
        registration_image_file=dict(),
    )
    inputs = MRTrix2TrackVis.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MRTrix2TrackVis_outputs():
    output_map = dict(out_file=dict(), )
    outputs = MRTrix2TrackVis.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
