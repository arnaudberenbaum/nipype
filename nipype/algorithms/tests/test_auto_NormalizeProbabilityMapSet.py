# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..misc import NormalizeProbabilityMapSet


def test_NormalizeProbabilityMapSet_inputs():
    input_map = dict(
        in_files=dict(),
        in_mask=dict(),
    )
    inputs = NormalizeProbabilityMapSet.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_NormalizeProbabilityMapSet_outputs():
    output_map = dict(out_files=dict(), )
    outputs = NormalizeProbabilityMapSet.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
