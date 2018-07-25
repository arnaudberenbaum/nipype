# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..featuredetection import DilateMask


def test_DilateMask_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputBinaryVolume=dict(argstr='--inputBinaryVolume %s', ),
        inputVolume=dict(argstr='--inputVolume %s', ),
        lowerThreshold=dict(argstr='--lowerThreshold %f', ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
        sizeStructuralElement=dict(argstr='--sizeStructuralElement %d', ),
    )
    inputs = DilateMask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DilateMask_outputs():
    output_map = dict(outputVolume=dict(), )
    outputs = DilateMask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
