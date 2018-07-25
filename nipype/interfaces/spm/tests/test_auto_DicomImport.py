# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import DicomImport


def test_DicomImport_inputs():
    input_map = dict(
        format=dict(
            field='convopts.format',
            usedefault=True,
        ),
        icedims=dict(
            field='convopts.icedims',
            usedefault=True,
        ),
        in_files=dict(
            field='data',
            mandatory=True,
        ),
        matlab_cmd=dict(),
        mfile=dict(usedefault=True, ),
        output_dir=dict(
            field='outdir',
            usedefault=True,
        ),
        output_dir_struct=dict(
            field='root',
            usedefault=True,
        ),
        paths=dict(),
        use_mcr=dict(),
        use_v8struct=dict(
            min_ver='8',
            usedefault=True,
        ),
    )
    inputs = DicomImport.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DicomImport_outputs():
    output_map = dict(out_files=dict(), )
    outputs = DicomImport.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
