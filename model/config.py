from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
from model.state import genesis_states
from model.psubs import partial_state_update_blocks

simulation_parameters = {
    'T': range(10),
    'N': 100,
}

exp = Experiment()
c = config_sim(simulation_parameters)
exp.append_configs(
    model_id="rps",
    initial_state=genesis_states,
    partial_state_update_blocks=partial_state_update_blocks,
    sim_configs=c
)