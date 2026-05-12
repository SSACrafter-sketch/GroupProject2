/********************* 
 * Animal_Words *
 *********************/


// store info about the experiment session:
let expName = 'animal_words';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);




flowScheduler.add(resultsscreenRoutineBegin());
flowScheduler.add(resultsscreenRoutineEachFrame());
flowScheduler.add(resultsscreenRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'stimuli/waldo.png', 'path': 'stimuli/waldo.png'},
    {'name': 'stimuli/correct.wav', 'path': 'stimuli/correct.wav'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.1.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  startinginstructions = new visual.TextBox({
    win: psychoJS.window,
    name: 'startinginstructions',
    text: 'This is a visual search task. This task will ask you to find waldo in a sea of candy canes.\n\nClick the star at every trial to begin.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  // Initialize components for Routine "start"
  startClock = new util.Clock();
  star = new visual.ShapeStim({
    win: psychoJS.window, name: 'star', 
    vertices: undefined, size: [0.035, 0.035],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color((1.0000, 0.9216, 0.8667)), 
    fillColor: new util.Color((1.0000, 0.9216, 0.8667)), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: 0, 
    interpolate: true, 
  });
  
  start_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  start_mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target', units : undefined, 
    image : 'stimuli/waldo.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.05, 0.125],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  trial_mouse = new core.Mouse({
    win: psychoJS.window,
  });
  trial_mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "correctsound"
  correctsoundClock = new util.Clock();
  correctSound = new sound.Sound({
      win: psychoJS.window,
      value: 'A',
      secs: 2.0,
      });
  correctSound.setVolume(1.0);
  correctSound.isPlaying = false;
  correctSound.isFinished = false;
  // Initialize components for Routine "resultsscreen"
  resultsscreenClock = new util.Clock();
  thanks = new visual.TextBox({
    win: psychoJS.window,
    name: 'thanks',
    text: 'Thank you for participating in this experiment.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.5],  units: undefined, 
    ori: 0.0,
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instructionsClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    instructionsMaxDuration = null
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(startinginstructions);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *startinginstructions* updates
    if (t >= 0.0 && startinginstructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startinginstructions.tStart = t;  // (not accounting for frame time here)
      startinginstructions.frameNStart = frameN;  // exact frame index
      
      startinginstructions.setAutoDraw(true);
    }
    
    
    // if startinginstructions is active this frame...
    if (startinginstructions.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (startinginstructions.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      startinginstructions.tStop = t;  // not accounting for scr refresh
      startinginstructions.frameNStop = frameN;  // exact frame index
      // update status
      startinginstructions.status = PsychoJS.Status.FINISHED;
      startinginstructions.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (instructionsMaxDurationReached) {
        instructionsClock.add(instructionsMaxDuration);
    } else {
        instructionsClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 10, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(startRoutineBegin(snapshot));
      trialsLoopScheduler.add(startRoutineEachFrame());
      trialsLoopScheduler.add(startRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(correctsoundRoutineBegin(snapshot));
      trialsLoopScheduler.add(correctsoundRoutineEachFrame());
      trialsLoopScheduler.add(correctsoundRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function startRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    startClock.reset();
    routineTimer.reset();
    startMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the start_mouse
    // current position of the mouse:
    start_mouse.x = [];
    start_mouse.y = [];
    start_mouse.leftButton = [];
    start_mouse.midButton = [];
    start_mouse.rightButton = [];
    start_mouse.time = [];
    start_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('start.started', globalClock.getTime());
    startMaxDuration = null
    // keep track of which components have finished
    startComponents = [];
    startComponents.push(star);
    startComponents.push(start_mouse);
    
    startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function startRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start' ---
    // get current time
    t = startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *star* updates
    if (t >= 0.0 && star.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      star.tStart = t;  // (not accounting for frame time here)
      star.frameNStart = frameN;  // exact frame index
      
      star.setAutoDraw(true);
    }
    
    
    // if star is active this frame...
    if (star.status === PsychoJS.Status.STARTED) {
    }
    
    // *start_mouse* updates
    if (t >= 0.0 && start_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_mouse.tStart = t;  // (not accounting for frame time here)
      start_mouse.frameNStart = frameN;  // exact frame index
      
      start_mouse.status = PsychoJS.Status.STARTED;
      start_mouse.mouseClock.reset();
      prevButtonState = start_mouse.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if start_mouse is active this frame...
    if (start_mouse.status === PsychoJS.Status.STARTED) {
      _mouseButtons = start_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          start_mouse.clickableObjects = eval(star)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(start_mouse.clickableObjects)) {
              start_mouse.clickableObjects = [start_mouse.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of start_mouse.clickableObjects) {
              if (obj.contains(start_mouse)) {
                  gotValidClick = true;
                  start_mouse.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              start_mouse.clicked_name.push(null);
          }
          _mouseXYs = start_mouse.getPos();
          start_mouse.x.push(_mouseXYs[0]);
          start_mouse.y.push(_mouseXYs[1]);
          start_mouse.leftButton.push(_mouseButtons[0]);
          start_mouse.midButton.push(_mouseButtons[1]);
          start_mouse.rightButton.push(_mouseButtons[2]);
          start_mouse.time.push(start_mouse.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function startRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start' ---
    startComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('start.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('start_mouse.x', start_mouse.x);
    psychoJS.experiment.addData('start_mouse.y', start_mouse.y);
    psychoJS.experiment.addData('start_mouse.leftButton', start_mouse.leftButton);
    psychoJS.experiment.addData('start_mouse.midButton', start_mouse.midButton);
    psychoJS.experiment.addData('start_mouse.rightButton', start_mouse.rightButton);
    psychoJS.experiment.addData('start_mouse.time', start_mouse.time);
    psychoJS.experiment.addData('start_mouse.clicked_name', start_mouse.clicked_name);
    
    // the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    trialClock.reset();
    routineTimer.reset();
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    target.setPos([(Math.random() - 0.5), (Math.random() - 0.5)]);
    // setup some python lists for storing info about the trial_mouse
    // current position of the mouse:
    trial_mouse.x = [];
    trial_mouse.y = [];
    trial_mouse.leftButton = [];
    trial_mouse.midButton = [];
    trial_mouse.rightButton = [];
    trial_mouse.time = [];
    trial_mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code
    import * as rnd from 'random';
    false_images = [];
    trial_mouse.clickReset();
    trial_mouse.setPos([0, 0]);
    mouseReleased = false;
    for (var i, _pj_c = 0, _pj_a = util.range(150), _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        i = _pj_a[_pj_c];
        pos = [rnd.uniform((- 0.5), 0.5), rnd.uniform((- 0.5), 0.5)];
        stim = new visual.ImageStim({"win": psychoJS.window, "image": "stimuli/candycane.png", "pos": pos, "size": [0.1, 0.1]});
        false_images.push(stim);
    }
    
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(target);
    trialComponents.push(trial_mouse);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *target* updates
    if (t >= 0.0 && target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target.tStart = t;  // (not accounting for frame time here)
      target.frameNStart = frameN;  // exact frame index
      
      target.setAutoDraw(true);
    }
    
    
    // if target is active this frame...
    if (target.status === PsychoJS.Status.STARTED) {
    }
    
    // *trial_mouse* updates
    if (t >= 0.0 && trial_mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_mouse.tStart = t;  // (not accounting for frame time here)
      trial_mouse.frameNStart = frameN;  // exact frame index
      
      trial_mouse.status = PsychoJS.Status.STARTED;
      trial_mouse.mouseClock.reset();
      prevButtonState = trial_mouse.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if trial_mouse is active this frame...
    if (trial_mouse.status === PsychoJS.Status.STARTED) {
      _mouseButtons = trial_mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          trial_mouse.clickableObjects = eval(target)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(trial_mouse.clickableObjects)) {
              trial_mouse.clickableObjects = [trial_mouse.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of trial_mouse.clickableObjects) {
              if (obj.contains(trial_mouse)) {
                  gotValidClick = true;
                  trial_mouse.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              trial_mouse.clicked_name.push(null);
          }
          _mouseXYs = trial_mouse.getPos();
          trial_mouse.x.push(_mouseXYs[0]);
          trial_mouse.y.push(_mouseXYs[1]);
          trial_mouse.leftButton.push(_mouseButtons[0]);
          trial_mouse.midButton.push(_mouseButtons[1]);
          trial_mouse.rightButton.push(_mouseButtons[2]);
          trial_mouse.time.push(trial_mouse.mouseClock.getTime());
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    // Run 'Each Frame' code from code
    for (var stim, _pj_c = 0, _pj_a = false_images, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        stim = _pj_a[_pj_c];
        stim.draw();
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('trial_mouse.x', trial_mouse.x);
    psychoJS.experiment.addData('trial_mouse.y', trial_mouse.y);
    psychoJS.experiment.addData('trial_mouse.leftButton', trial_mouse.leftButton);
    psychoJS.experiment.addData('trial_mouse.midButton', trial_mouse.midButton);
    psychoJS.experiment.addData('trial_mouse.rightButton', trial_mouse.rightButton);
    psychoJS.experiment.addData('trial_mouse.time', trial_mouse.time);
    psychoJS.experiment.addData('trial_mouse.clicked_name', trial_mouse.clicked_name);
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function correctsoundRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'correctsound' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    correctsoundClock.reset(routineTimer.getTime());
    routineTimer.add(2.000000);
    correctsoundMaxDurationReached = false;
    // update component parameters for each repeat
    correctSound.isFinished = false;
    correctSound.setValue('stimuli/correct.wav');
    correctSound.secs=2.0;
    correctSound.setVolume(1.0);
    psychoJS.experiment.addData('correctsound.started', globalClock.getTime());
    correctsoundMaxDuration = null
    // keep track of which components have finished
    correctsoundComponents = [];
    correctsoundComponents.push(correctSound);
    
    correctsoundComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function correctsoundRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'correctsound' ---
    // get current time
    t = correctsoundClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    if (correctSound.status === STARTED) {
        correctSound.isPlaying = true;
        if (t >= (correctSound.getDuration() + correctSound.tStart)) {
            correctSound.isFinished = true;
        }
    }
    // start/stop correctSound
    if (t >= 0 && correctSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      correctSound.tStart = t;  // (not accounting for frame time here)
      correctSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ correctSound.play(); });  // screen flip
      correctSound.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (correctSound.status === PsychoJS.Status.STARTED && t >= frameRemains || correctSound.isFinished) {
      // keep track of stop time/frame for later
      correctSound.tStop = t;  // not accounting for scr refresh
      correctSound.frameNStop = frameN;  // exact frame index
      // update status
      correctSound.status = PsychoJS.Status.FINISHED;
      // stop playback
      correctSound.stop();
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    correctsoundComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function correctsoundRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'correctsound' ---
    correctsoundComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('correctsound.stopped', globalClock.getTime());
    correctSound.stop();  // ensure sound has stopped at end of Routine
    if (routineForceEnded) {
        routineTimer.reset();} else if (correctsoundMaxDurationReached) {
        correctsoundClock.add(correctsoundMaxDuration);
    } else {
        correctsoundClock.add(2.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function resultsscreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'resultsscreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    resultsscreenClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    resultsscreenMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('resultsscreen.started', globalClock.getTime());
    resultsscreenMaxDuration = null
    // keep track of which components have finished
    resultsscreenComponents = [];
    resultsscreenComponents.push(thanks);
    
    resultsscreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function resultsscreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'resultsscreen' ---
    // get current time
    t = resultsscreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thanks* updates
    if (t >= 0.0 && thanks.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thanks.tStart = t;  // (not accounting for frame time here)
      thanks.frameNStart = frameN;  // exact frame index
      
      thanks.setAutoDraw(true);
    }
    
    
    // if thanks is active this frame...
    if (thanks.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (thanks.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      thanks.tStop = t;  // not accounting for scr refresh
      thanks.frameNStop = frameN;  // exact frame index
      // update status
      thanks.status = PsychoJS.Status.FINISHED;
      thanks.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    resultsscreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function resultsscreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'resultsscreen' ---
    resultsscreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('resultsscreen.stopped', globalClock.getTime());
    if (routineForceEnded) {
        routineTimer.reset();} else if (resultsscreenMaxDurationReached) {
        resultsscreenClock.add(resultsscreenMaxDuration);
    } else {
        resultsscreenClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
