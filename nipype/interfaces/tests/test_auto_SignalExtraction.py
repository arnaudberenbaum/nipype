# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..nilearn import SignalExtraction


def test_SignalExtraction_inputs():
    input_map = dict(
        class_labels=dict(mandatory=True, ),
        detrend=dict(usedefault=True, ),
        in_file=dict(mandatory=True, ),
        incl_shared_variance=dict(usedefault=True, ),
        include_global=dict(usedefault=True, ),
        label_files=dict(mandatory=True, ),
        out_file=dict(usedefault=True, ),
    )
    inputs = SignalExtraction.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SignalExtraction_outputs():
    output_map = dict(out_file=dict(), )
    outputs = SignalExtraction.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
