# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Dot


def test_Dot_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        demean=dict(argstr='-demean', ),
        docoef=dict(argstr='-docoef', ),
        docor=dict(argstr='-docor', ),
        dodice=dict(argstr='-dodice', ),
        dodot=dict(argstr='-dodot', ),
        doeta2=dict(argstr='-doeta2', ),
        dosums=dict(argstr='-dosums', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        full=dict(argstr='-full', ),
        in_files=dict(
            argstr='%s ...',
            position=-2,
        ),
        mask=dict(argstr='-mask %s', ),
        mrange=dict(argstr='-mrange %s %s', ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr=' |& tee %s',
            position=-1,
        ),
        outputtype=dict(),
        show_labels=dict(argstr='-show_labels', ),
        upper=dict(argstr='-upper', ),
    )
    inputs = Dot.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Dot_outputs():
    output_map = dict(out_file=dict(), )
    outputs = Dot.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
