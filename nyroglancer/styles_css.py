# replaced every \ with \\
content='''
/**
 * @license
 * Copyright 2016 Google Inc.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#statusContainer{position:fixed;bottom:0;z-index:100;background-color:grey;color:#fff;margin:0;padding:0}#statusContainer li{width:100vw;max-height:25vh;overflow-y:auto}.rendered-data-panel{cursor:crosshair;position:relative}.noselect{-webkit-touch-callout:none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none}label.perspective-panel-show-slice-views{pointer-events:none}input.perspective-panel-show-slice-views{pointer-events:all}body,html{margin:0;padding:0;overflow:hidden;width:100vw;height:100vh;background-color:#000;color:#fff}body{position:relative;display:flex;flex-direction:column}.overlay{height:100%;width:100%;position:fixed;z-index:99;top:0;left:0;background-color:rgba(0,0,0,.8)}.overlay-content{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background-color:#fff;z-index:100;color:#000;padding:1em}.describe-key-bindings{overflow-x:hidden}.describe-key-bindings .dl{overflow-y:scroll;max-height:80vh;overflow-x:hidden}.describe-key-bindings .definition-outer-container{display:block}.describe-key-bindings .definition-container{display:inline-block;white-space:nowrap}.describe-key-bindings .dt{font-family:monospace;font-weight:700;display:inline-block;width:20ch}.describe-key-bindings .dd{display:inline-block}.segment-set-widget button{margin:3px}.segment-set-widget{flex:1;overflow-y:auto}.segment-set-widget .item-container{flex:1;display:flex;flex-wrap:wrap}.scale-bar-container{text-align:center;background-color:rgba(0,0,0,.3);position:absolute;left:1em;bottom:1em;padding:2px;font-weight:700;pointer-events:none}.scale-bar{min-height:1ex;background-color:#fff;padding:0;margin:0;margin-top:2px}.uint64-entry input{width:19ch}.uint64-entry input.invalid-input{color:red}.range-slider{display:flex;flex-direction:row;white-space:nowrap;justify-content:space-between}.segmentation-dropdown .add-segment label:before{content:"+ ";font-weight:700}.segmentation-dropdown .add-segment{margin-bottom:5px}.autocomplete-hint,.autocomplete-input{outline:0;width:100%;border:0;margin:0;padding:0}.autocomplete-completion,.autocomplete-hint,.autocomplete-input,.autocomplete-prompt{font-family:monospace;font-size:medium}.autocomplete{display:flex;flex-direction:row}.autocomplete-prompt{display:inline-block}.autocomplete-prompt:not(:empty){margin-right:1em}.autocomplete-hint{position:absolute;top:0;left:0;border-color:transparent;background-color:transparent;box-shadow:none;color:#aaa}.autocomplete-dropdown-wrapper{display:inline-block;position:relative;border:0;margin:0;padding:0;flex:1}.autocomplete-input{position:relative;top:0;left:0;color:#333;background-color:transparent}.autocomplete-input-wrapper{display:flex;position:relative;outline:0;border:0;margin:0;padding:0;left:0;right:0;bottom:0;top:0}.autocomplete-dropdown{position:absolute;display:none;outline:0;margin:0;padding:0;text-align:left;cursor:default;border:1px solid #aaa;overflow-y:scroll;overflow-x:hidden;white-space:pre;background-color:#fff}.autocomplete-completion:hover{outline:1px solid #ddd}.autocomplete-completion-active{background-color:#ccc}.autocomplete-completion-with-description{display:flex;flex-direction:row}.autocomplete-completion-description{text-align:right;display:inline;flex:1;font-style:italic;padding-left:2em}.add-layer-overlay{width:80vw}.add-layer-name{display:flex;flex-direction:row;font-family:monospace}.add-layer-overlay .dialog-status{width:100%;height:4em;overflow:auto}.add-layer-overlay form{display:flex;flex-direction:row;width:100%;margin-bottom:5px}.add-layer-overlay form button{margin-left:1em}.add-layer-overlay form>label{margin-right:1em;min-width:4em}.add-layer-name,.add-layer-source{border:1px solid #000;padding:2px;flex:1}.add-layer-name.invalid-input{border:1px solid red}.add-layer-overlay .add-layer-name{font-family:monospace;flex:1;outline:0;margin:0}.add-layer-overlay .dialog-status.dialog-status-error{color:red}.layer-panel{width:100%;display:flex;flex-direction:row}.layer-item+.layer-add-button,.layer-item+.layer-item{margin-left:5px}.layer-item{position:relative;display:flex;align-items:center;color:#fff;cursor:pointer;border:1px solid #ccc}.layer-add-button,.layer-item{margin:2px}.layer-item-parent:hover .layer-item{border-color:#daa520}.clear-button:after{content:"x"}.layer-dropdown{display:none;position:absolute;flex-direction:column;min-width:100%;background-color:#000;padding:5px;border:1px solid #fff;box-sizing:border-box;z-index:200}.layer-item-parent{display:inline-block;background-color:#000}.layer-item-parent:not(.sortable-chosen){position:relative}.layer-item-label{display:inline-block;background-color:#222;padding-right:3px}.layer-item-number{display:inline-block;background-color:#9a7518;font-weight:700;padding:1px;margin:3px}.layer-item-value{display:inline-block;min-width:10ch;margin-left:1ch;text-align:center}.layer-item-close:before{content:"\\274C"}.layer-item-close{display:flex;align-items:center;justify-content:center;font-size:16px;border-radius:50%;width:1.7ex;height:1.7ex;font-family:sans-serif;padding:1px;color:#fff;position:relative}.layer-item-close:hover{background-color:#db4437}.layer-item[layer-visible=false] .layer-item-label{text-decoration:line-through}.layer-add-button:before{font-weight:700;content:"+"}.layer-item[layer-visible=false]{color:#bbb}.position-status-panel{background-color:#000;color:#fff;overflow:hidden;white-space:nowrap}input.position-status-coord,label.position-status-coord{font-family:monospace;color:#fff}input.position-status-coord{background-color:#000;border:0;width:9ch;margin-left:5px;margin-right:5px}.position-status-mouse{font-family:monospace;color:orange;white-space:pre}label.position-status-coord:hover{color:orange}#container .gl-canvas{position:absolute;top:0;left:0;width:100%;height:100%;z-index:0}#container{width:100vw;flex:1;position:relative}.gllayoutcontainer{display:flex;flex-direction:column;position:absolute;top:0;left:0;width:100%;height:100%;z-index:2}.gllayoutrow{flex:1;display:flex;flex-direction:row}.gllayoutcell{border:2px solid #000;flex:1}.gllayoutcell[isActivePanel=true]{border-color:#fff}.help-button{text-weight:bold}
'''