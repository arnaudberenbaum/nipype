# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..petpvc import PETPVC


def test_PETPVC_inputs():
    input_map = dict(
        alpha=dict(
            argstr='-a %.4f',
            usedefault=True,
        ),
        args=dict(argstr='%s', ),
        debug=dict(
            argstr='-d',
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fwhm_x=dict(
            argstr='-x %.4f',
            mandatory=True,
        ),
        fwhm_y=dict(
            argstr='-y %.4f',
            mandatory=True,
        ),
        fwhm_z=dict(
            argstr='-z %.4f',
            mandatory=True,
        ),
        in_file=dict(
            argstr='-i %s',
            mandatory=True,
        ),
        mask_file=dict(
            argstr='-m %s',
            mandatory=True,
        ),
        n_deconv=dict(
            argstr='-k %d',
            usedefault=True,
        ),
        n_iter=dict(
            argstr='-n %d',
            usedefault=True,
        ),
        out_file=dict(
            argstr='-o %s',
            genfile=True,
            hash_files=False,
        ),
        pvc=dict(
            argstr='-p %s',
            mandatory=True,
        ),
        stop_crit=dict(
            argstr='-a %.4f',
            usedefault=True,
        ),
    )
    inputs = PETPVC.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_PETPVC_outputs():
    output_map = dict(out_file=dict(), )
    outputs = PETPVC.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
