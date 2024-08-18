from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display, HTML
import ipywidgets as widgets

# basic info

query_sequence_w = widgets.Text(
    value='PIAQIHILEGRSDEQKETLIREVSEAISRSLDAPLTSVRVIITEMAKGHFGIGGELASK',
    placeholder='Insert query sequence here',
    description='query_sequence:',
)

jobname_w = widgets.Text(
    value='test',
    placeholder='Insert job name',
    description='jobname:',
)

num_relax_w = widgets.Dropdown(
    options=[0, 1, 5],
    value=0,
    description='num_relax:',
)

template_mode_w = widgets.Dropdown(
    options=['none', 'pdb100', 'custom'],
    value='none',
    description='template_mode:',
)

display(HTML('<h2>Input protein sequence(s), then hit Run -> Run All Cells</h2>'))

display(query_sequence_w)
display(HTML('<p>Use : to specify inter-protein chainbreaks ' \
             'for <b>modeling complexes</b> (supports homo- and ' \
             'hetro-oligomers). For example <b>PI...SK:PI...SK</b> ' \
             'for a homodimer</p>'))

display(jobname_w)

display(num_relax_w)
display(HTML('<p>specify how many of the top ranked structures ' \
             'to relax using amber</p>'))

display(template_mode_w)
display(HTML('<p>none = no template information is used. ' \
              'pdb100 = detect templates in pdb100 (see notes). ' \
              'custom - upload and search own templates ' \
              '(PDB or mmCIF format, see notes)</p>'))

# MSA options

msa_mode_w = widgets.Dropdown(
    options=['mmseqs2_uniref_env', 'mmseqs2_uniref', 'single_sequence', 'custom'],
    value='mmseqs2_uniref_env',
    description='msa_mode:'
)

custom_msa_w = widgets.Text(
    value='',
    placeholder='Filepath to custom MSA (if using custom)',
    description='custom_msa:',
)

pair_mode_w = widgets.Dropdown(
    options=['unpaired_paired', 'paired', 'unpaired'],
    value='unpaired_paired',
    description='pair_mode:'
)

display(HTML('<h3>MSA options (custom MSA upload, single sequence, pairing mode)</h3>'))

display(msa_mode_w)

display(custom_msa_w)

display(pair_mode_w)
display(HTML('<p>"unpaired_paired" = pair sequences from same ' \
             'species + unpaired MSA, "unpaired" = seperate MSA ' \
             'for each chain, "paired" - only use paired sequences.</p>'))

# Advanced settings

model_type_w = widgets.Dropdown(
    options=["auto", "alphafold2_ptm", "alphafold2_multimer_v1", "alphafold2_multimer_v2", "alphafold2_multimer_v3", "deepfold_v1"],
    value="auto",
    description="model_type:"
)

num_recycles_w = widgets.Dropdown(
    options=["auto", "0", "1", "3", "6", "12", "24", "48"],
    value="3",
    description="num_recycles:"
)

recycle_early_stop_tolerance_w = widgets.Dropdown(
    options=["auto", "0", "1", "3", "6", "12", "24", "48"],
    value="auto",
    description="recycle_early_stop_tolerance:"
)

relax_max_iterations_w = widgets.Dropdown(
    options=["0", "200", "2000"],
    value="200",
    description="relax_max_iterations:"
)

pairing_strategy_w = widgets.Dropdown(
    options=["greedy", "complete"],
    value="greedy",
    description="pairing_strategy:"
)

display(HTML('<h3>Advanced settings</h3>'))

display(model_type_w)
display(HTML('<p>if auto selected, will use alphafold2_ptm for monomer prediction and alphafold2_multimer_v3 for complex prediction. Any of the mode_types can be used (regardless if input is monomer or complex).</p>'))

display(num_recycles_w)
display(HTML('<p>if auto selected, will use num_recycles=20 if model_type=alphafold2_multimer_v3, else num_recycles=3.</p>'))

display(recycle_early_stop_tolerance_w)
display(HTML('<p>if auto selected, will use tol=0.5 if model_type=alphafold2_multimer_v3 else tol=0.0.</p>'))

display(relax_max_iterations_w)
display(HTML('<p>max amber relax iterations, 0 = unlimited (AlphaFold2 default, can take very long)</p>'))

display(pairing_strategy_w)
display(HTML('<p>greedy = pair any taxonomically matching subsets, complete = all sequences have to match in one line.</p>'))

# Sample settings

max_msa_w = widgets.Dropdown(
    options=["auto", "512:1024", "256:512", "64:128", "32:64", "16:32"],
    value="auto",
    description="max_msa:"
)

num_seeds_w = widgets.Dropdown(
    options=[1, 2, 4, 8, 16],
    value=1,
    description="num_seeds:"
)

use_dropout_w = widgets.Checkbox(
    value=False,
    description="use_dropout:",
)

display(HTML('<h3>Sample settings</h3>'))
display(HTML('<p>enable dropouts and increase number of seeds to sample predictions from uncertainty of the model.</p>'))
display(HTML('<p>decrease max_msa to increase uncertainty</p>'))

display(max_msa_w)
display(num_seeds_w)
a = widgets.Label("testing")
display(a)
display(use_dropout_w)

# Save settings

save_all_w = widgets.Checkbox(
    value=False,
    description="save_all:"
)

save_recycles_w = widgets.Checkbox(
    value=False,
    description="save_recycles:"
)

dpi_w = widgets.IntText(
    value=200,
    description="dpi:"
)

display(HTML('<h3>Save settings</h3>'))
display(save_all_w)
display(save_recycles_w)
display(dpi_w)
display(HTML('<p>set dpi for image resolution</p>'))

# Run prediction

display_images_w = widgets.Checkbox(
    value=True,
    description="display_images:"
)

display(HTML('<h3>Run prediction</h3>'))
display(display_images_w)

# Display 3D structure

rank_num_w = widgets.Dropdown(
    options=[1, 2, 3, 4, 5],
    value=1,
    description="rank_num:"
)

color_w = widgets.Dropdown(
    options=["chain", "lDDT", "rainbow"],
    value="lDDT",
    description="color:"
)

show_sidechains_w = widgets.Checkbox(
    value=False,
    description="show_sidechains:"
)

show_mainchains_w = widgets.Checkbox(
    value=False,
    description="show_mainchains:"
)

display(HTML('<h3>Display 3D structure</h3>'))

display(rank_num_w)
display(color_w)
display(show_sidechains_w)
display(show_mainchains_w)