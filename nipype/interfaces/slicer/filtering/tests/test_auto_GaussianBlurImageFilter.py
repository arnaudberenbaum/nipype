# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..denoising import GaussianBlurImageFilter


def test_GaussianBlurImageFilter_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputVolume=dict(
            argstr='%s',
            position=-2,
        ),
        outputVolume=dict(
            argstr='%s',
            hash_files=False,
            position=-1,
        ),
        sigma=dict(argstr='--sigma %f', ),
    )
    inputs = GaussianBlurImageFilter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_GaussianBlurImageFilter_outputs():
    output_map = dict(outputVolume=dict(position=-1, ), )
    outputs = GaussianBlurImageFilter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
