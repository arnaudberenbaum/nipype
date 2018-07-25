# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..gtract import gtractResampleCodeImage


def test_gtractResampleCodeImage_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputCodeVolume=dict(argstr='--inputCodeVolume %s', ),
        inputReferenceVolume=dict(argstr='--inputReferenceVolume %s', ),
        inputTransform=dict(argstr='--inputTransform %s', ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
        transformType=dict(argstr='--transformType %s', ),
    )
    inputs = gtractResampleCodeImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_gtractResampleCodeImage_outputs():
    output_map = dict(outputVolume=dict(), )
    outputs = gtractResampleCodeImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
