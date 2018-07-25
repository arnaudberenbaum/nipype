# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import ResponseSD


def test_ResponseSD_inputs():
    input_map = dict(
        algorithm=dict(
            argstr='%s',
            mandatory=True,
            position=1,
        ),
        args=dict(argstr='%s', ),
        bval_scale=dict(argstr='-bvalue_scaling %s', ),
        csf_file=dict(
            argstr='%s',
            position=-1,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        gm_file=dict(
            argstr='%s',
            position=-2,
        ),
        grad_file=dict(argstr='-grad %s', ),
        grad_fsl=dict(argstr='-fslgrad %s %s', ),
        in_bval=dict(),
        in_bvec=dict(argstr='-fslgrad %s %s', ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=-5,
        ),
        in_mask=dict(argstr='-mask %s', ),
        max_sh=dict(
            argstr='-lmax %s',
            sep=',',
            usedefault=True,
        ),
        mtt_file=dict(
            argstr='%s',
            position=-4,
        ),
        nthreads=dict(
            argstr='-nthreads %d',
            nohash=True,
        ),
        wm_file=dict(
            argstr='%s',
            position=-3,
            usedefault=True,
        ),
    )
    inputs = ResponseSD.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ResponseSD_outputs():
    output_map = dict(
        csf_file=dict(argstr='%s', ),
        gm_file=dict(argstr='%s', ),
        wm_file=dict(argstr='%s', ),
    )
    outputs = ResponseSD.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
