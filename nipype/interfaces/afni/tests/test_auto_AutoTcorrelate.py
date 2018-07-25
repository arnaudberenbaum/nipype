# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import AutoTcorrelate


def test_AutoTcorrelate_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        eta2=dict(argstr='-eta2', ),
        in_file=dict(
            argstr='%s',
            copyfile=False,
            mandatory=True,
            position=-1,
        ),
        mask=dict(argstr='-mask %s', ),
        mask_only_targets=dict(
            argstr='-mask_only_targets',
            xor=['mask_source'],
        ),
        mask_source=dict(
            argstr='-mask_source %s',
            xor=['mask_only_targets'],
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr='-prefix %s',
            name_source='in_file',
            name_template='%s_similarity_matrix.1D',
        ),
        outputtype=dict(),
        polort=dict(argstr='-polort %d', ),
    )
    inputs = AutoTcorrelate.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_AutoTcorrelate_outputs():
    output_map = dict(out_file=dict(), )
    outputs = AutoTcorrelate.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
