{
  "targets": [
    {
      "target_name": "uvrun2",
      "sources": ["uvrun2.cc"],
      "variables": {
        "node_version": '<!(node --version | sed -e "s/^v\([0-9]*\)\\.\([0-9]*\)\\.\([0-9]*\).*$/\\1.\\2/")',
      },
      "target_conditions": [
        [ "node_version == '0.8'", { "defines": ["NODE_0_8"] } ],
        [ "node_version == '0.9'", { "defines": ["NODE_0_9"] } ],
        [ "node_version == '0.10'", { "defines": ["NODE_0_10"] } ],
        [ "node_version == '0.11'", { "defines": ["NODE_0_11"] } ],
        [ "node_version == '0.12'", { "defines": ["NODE_0_12"] } ],
        [ "node_version == '0.13'", { "defines": ["NODE_0_13"] } ]
      ]
    }
  ]
}
