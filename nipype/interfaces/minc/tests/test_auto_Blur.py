# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..minc import Blur


def test_Blur_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        clobber=dict(
            argstr='-clobber',
            usedefault=True,
        ),
        dimensions=dict(argstr='-dimensions %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fwhm=dict(
            argstr='-fwhm %s',
            mandatory=True,
            xor=('fwhm', 'fwhm3d', 'standard_dev'),
        ),
        fwhm3d=dict(
            argstr='-3dfwhm %s %s %s',
            mandatory=True,
            xor=('fwhm', 'fwhm3d', 'standard_dev'),
        ),
        gaussian=dict(
            argstr='-gaussian',
            xor=('gaussian', 'rect'),
        ),
        gradient=dict(argstr='-gradient', ),
        input_file=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        no_apodize=dict(argstr='-no_apodize', ),
        output_file_base=dict(
            argstr='%s',
            position=-1,
        ),
        partial=dict(argstr='-partial', ),
        rect=dict(
            argstr='-rect',
            xor=('gaussian', 'rect'),
        ),
        standard_dev=dict(
            argstr='-standarddev %s',
            mandatory=True,
            xor=('fwhm', 'fwhm3d', 'standard_dev'),
        ),
    )
    inputs = Blur.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Blur_outputs():
    output_map = dict(
        gradient_dxyz=dict(),
        output_file=dict(),
        partial_dx=dict(),
        partial_dxyz=dict(),
        partial_dy=dict(),
        partial_dz=dict(),
    )
    outputs = Blur.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
