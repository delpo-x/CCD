"""PROOF OF CONCEPT (non e' codice di produzione) - ticket 02 stato di partita.

Uso:
  python poc_load_state.py dump  <game.yml> <state.json>   # dry-run a1..a8 (mock), salva lo stato
  python poc_load_state.py pack  <state.json> <out_dir>    # carica JSON, salta gli agenti LLM, esegue solo a8_5 + a9

Dimostra che GameState e' serializzabile con model_dump_json / model_validate_json e che
un grafo ridotto [a8_5_host_images -> a9_packaging] produce il pacchetto senza alcuna chiamata LLM.
"""
import sys
from pathlib import Path

from langgraph.graph import END, START, StateGraph

from mystery_agents.graph import workflow as w
from mystery_agents.models.state import GameConfig, GameState, MetaInfo, PlayerConfig


def dump(yml: str, out: str) -> None:
    st = GameState(meta=MetaInfo(), config=GameConfig(
        players=PlayerConfig(total=6), generate_images=False, dry_run=True, config_file=yml))
    for node in (w.a1_config_node, w.a2_world_node, w.v1_world_validator_node,
                 w.a2_5_visual_style_node, w.a3_characters_node, w.a4_relationships_node,
                 w.a5_crime_node, w.a6_timeline_node, w.a7_killer_node,
                 w.v2_game_logic_validator_node, w.a8_content_node):
        st = node(st)
    Path(out).write_text(st.model_dump_json(indent=2), encoding="utf-8")


def pack(state_json: str, out_dir: str) -> None:
    st = GameState.model_validate_json(Path(state_json).read_text(encoding="utf-8"))
    st.config.dry_run = False          # prova: nessun mock, nessun LLM
    st.config.generate_images = False  # a8_5 fa return immediato
    g = StateGraph(GameState)
    g.add_node("a8_5", w.a8_5_host_images_node)
    g.add_node("a9", lambda s: _a9(s, out_dir))
    g.add_edge(START, "a8_5"); g.add_edge("a8_5", "a9"); g.add_edge("a9", END)
    res = g.compile().invoke(st)
    print("packaging:", res["packaging"].index_summary.splitlines()[-1] if isinstance(res, dict) else res.packaging)


def _a9(s: GameState, out_dir: str) -> GameState:
    from mystery_agents.agents.a9_packaging import PackagingAgent
    from mystery_agents.utils.cache import AgentFactory
    return AgentFactory.get_agent(PackagingAgent).run(s, output_dir=out_dir)


if __name__ == "__main__":
    {"dump": lambda: dump(sys.argv[2], sys.argv[3]), "pack": lambda: pack(sys.argv[2], sys.argv[3])}[sys.argv[1]]()
