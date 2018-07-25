# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..model import Remlfit


def test_Remlfit_inputs():
    input_map = dict(
        STATmask=dict(argstr='-STATmask %s', ),
        addbase=dict(
            argstr='-addbase %s',
            copyfile=False,
            sep=' ',
        ),
        args=dict(argstr='%s', ),
        automask=dict(
            argstr='-automask',
            usedefault=True,
        ),
        dsort=dict(
            argstr='-dsort %s',
            copyfile=False,
        ),
        dsort_nods=dict(
            argstr='-dsort_nods',
            requires=['dsort'],
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        errts_file=dict(argstr='-Rerrts %s', ),
        fitts_file=dict(argstr='-Rfitts %s', ),
        fout=dict(argstr='-fout', ),
        glt_file=dict(argstr='-Rglt %s', ),
        gltsym=dict(argstr='-gltsym "%s" %s...', ),
        in_files=dict(
            argstr='-input "%s"',
            copyfile=False,
            mandatory=True,
            sep=' ',
        ),
        mask=dict(argstr='-mask %s', ),
        matim=dict(
            argstr='-matim %s',
            xor=['matrix'],
        ),
        matrix=dict(
            argstr='-matrix %s',
            mandatory=True,
        ),
        nobout=dict(argstr='-nobout', ),
        nodmbase=dict(
            argstr='-nodmbase',
            requires=['addbase', 'dsort'],
        ),
        nofdr=dict(argstr='-noFDR', ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        obeta=dict(argstr='-Obeta %s', ),
        obuck=dict(argstr='-Obuck %s', ),
        oerrts=dict(argstr='-Oerrts %s', ),
        ofitts=dict(argstr='-Ofitts %s', ),
        oglt=dict(argstr='-Oglt %s', ),
        out_file=dict(argstr='-Rbuck %s', ),
        outputtype=dict(),
        ovar=dict(argstr='-Ovar %s', ),
        polort=dict(
            argstr='-polort %d',
            xor=['matrix'],
        ),
        quiet=dict(argstr='-quiet', ),
        rbeta_file=dict(argstr='-Rbeta %s', ),
        rout=dict(argstr='-rout', ),
        slibase=dict(argstr='-slibase %s', ),
        slibase_sm=dict(argstr='-slibase_sm %s', ),
        tout=dict(argstr='-tout', ),
        usetemp=dict(argstr='-usetemp', ),
        var_file=dict(argstr='-Rvar %s', ),
        verb=dict(argstr='-verb', ),
        wherr_file=dict(argstr='-Rwherr %s', ),
    )
    inputs = Remlfit.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Remlfit_outputs():
    output_map = dict(
        errts_file=dict(),
        fitts_file=dict(),
        glt_file=dict(),
        obeta=dict(),
        obuck=dict(),
        oerrts=dict(),
        ofitts=dict(),
        oglt=dict(),
        out_file=dict(),
        ovar=dict(),
        rbeta_file=dict(),
        var_file=dict(),
        wherr_file=dict(),
    )
    outputs = Remlfit.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
