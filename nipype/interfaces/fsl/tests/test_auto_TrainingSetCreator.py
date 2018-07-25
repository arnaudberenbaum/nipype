# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..fix import TrainingSetCreator


def test_TrainingSetCreator_inputs():
    input_map = dict(
        mel_icas_in=dict(
            argstr='%s',
            copyfile=False,
            position=-1,
        ), )
    inputs = TrainingSetCreator.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_TrainingSetCreator_outputs():
    output_map = dict(
        mel_icas_out=dict(
            argstr='%s',
            copyfile=False,
            position=-1,
        ), )
    outputs = TrainingSetCreator.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
