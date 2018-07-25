# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import TNorm


def test_TNorm_inputs():
    input_map = dict(
        L1fit=dict(argstr='-L1fit', ),
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            copyfile=False,
            mandatory=True,
            position=-1,
        ),
        norm1=dict(argstr='-norm1', ),
        norm2=dict(argstr='-norm2', ),
        normR=dict(argstr='-normR', ),
        normx=dict(argstr='-normx', ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr='-prefix %s',
            name_source='in_file',
            name_template='%s_tnorm',
        ),
        outputtype=dict(),
        polort=dict(argstr='-polort %s', ),
    )
    inputs = TNorm.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_TNorm_outputs():
    output_map = dict(out_file=dict(), )
    outputs = TNorm.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
