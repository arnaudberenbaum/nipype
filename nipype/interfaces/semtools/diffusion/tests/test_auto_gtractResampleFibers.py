# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..gtract import gtractResampleFibers


def test_gtractResampleFibers_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputForwardDeformationFieldVolume=dict(
            argstr='--inputForwardDeformationFieldVolume %s', ),
        inputReverseDeformationFieldVolume=dict(
            argstr='--inputReverseDeformationFieldVolume %s', ),
        inputTract=dict(argstr='--inputTract %s', ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        outputTract=dict(
            argstr='--outputTract %s',
            hash_files=False,
        ),
        writeXMLPolyDataFile=dict(argstr='--writeXMLPolyDataFile ', ),
    )
    inputs = gtractResampleFibers.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_gtractResampleFibers_outputs():
    output_map = dict(outputTract=dict(), )
    outputs = gtractResampleFibers.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
