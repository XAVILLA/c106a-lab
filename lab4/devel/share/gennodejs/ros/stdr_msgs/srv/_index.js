
"use strict";

let DeleteCO2Source = require('./DeleteCO2Source.js')
let DeleteSoundSource = require('./DeleteSoundSource.js')
let DeleteRfidTag = require('./DeleteRfidTag.js')
let AddThermalSource = require('./AddThermalSource.js')
let RegisterGui = require('./RegisterGui.js')
let AddCO2Source = require('./AddCO2Source.js')
let LoadExternalMap = require('./LoadExternalMap.js')
let DeleteThermalSource = require('./DeleteThermalSource.js')
let MoveRobot = require('./MoveRobot.js')
let AddSoundSource = require('./AddSoundSource.js')
let AddRfidTag = require('./AddRfidTag.js')
let LoadMap = require('./LoadMap.js')

module.exports = {
  DeleteCO2Source: DeleteCO2Source,
  DeleteSoundSource: DeleteSoundSource,
  DeleteRfidTag: DeleteRfidTag,
  AddThermalSource: AddThermalSource,
  RegisterGui: RegisterGui,
  AddCO2Source: AddCO2Source,
  LoadExternalMap: LoadExternalMap,
  DeleteThermalSource: DeleteThermalSource,
  MoveRobot: MoveRobot,
  AddSoundSource: AddSoundSource,
  AddRfidTag: AddRfidTag,
  LoadMap: LoadMap,
};
