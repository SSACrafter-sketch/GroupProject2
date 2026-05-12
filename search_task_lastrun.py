#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.3),
    on Mon May 11 22:52:14 2026
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.3'
expName = 'animal_words'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/sienna/Downloads/GroupProject2-main/search_task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instructions0" ---
    textbox = visual.TextBox2(
         win, text='This is a visual search task. This task will ask you to find Waldo in a sea of candy canes.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "waldodemo1" ---
    demo1 = visual.ImageStim(
        win=win,
        name='demo1', 
        image='stimuli/waldo.png', mask=None, anchor='center',
        ori=0.0, pos=(0.05, -.10), draggable=False, size=(0.45, 0.85),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    democlick1 = event.Mouse(win=win)
    x, y = [None, None]
    democlick1.mouseClock = core.Clock()
    demoinstructions1 = visual.TextBox2(
         win, text='Try clicking Waldo.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.4), draggable=False,      letterHeight=0.05,
         size=(0.4, 0.4), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='demoinstructions1',
         depth=-2, autoLog=True,
    )
    
    # --- Initialize components for Routine "correctsound" ---
    # set audio backend
    sound.Sound.backend = 'ptb'
    correctSound = sound.Sound(
        'A', 
        secs=2.0, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='correctSound'
    )
    correctSound.setVolume(1.0)
    
    # --- Initialize components for Routine "clickthestar" ---
    clickstar = visual.TextBox2(
         win, text='Great! Now find Waldo.\n\nClick the star at every trial to begin.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='clickstar',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "start" ---
    star = visual.ShapeStim(
        win=win, name='star', vertices='star7',
        size=(0.035, 0.035),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=(1.0000, 0.9216, 0.8667), fillColor=(1.0000, 0.9216, 0.8667),
        opacity=None, depth=0.0, interpolate=True)
    start_mouse = event.Mouse(win=win)
    x, y = [None, None]
    start_mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial1" ---
    target1 = visual.ImageStim(
        win=win,
        name='target1', 
        image='stimuli/waldo.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.05, 0.125),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    trial_mouse = event.Mouse(win=win)
    x, y = [None, None]
    trial_mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "correctsound" ---
    correctSound = sound.Sound(
        'A', 
        secs=2.0, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='correctSound'
    )
    correctSound.setVolume(1.0)
    
    # --- Initialize components for Routine "instructions1" ---
    secondtrial = visual.TextBox2(
         win, text='Great job!\n\nNow we will ask you to find Waldo when he’s wearing a different outfit…', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='secondtrial',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "waldodemo2" ---
    demo2 = visual.ImageStim(
        win=win,
        name='demo2', 
        image='stimuli/waldo1.png', mask=None, anchor='center',
        ori=0.0, pos=(0.04, -0.10), draggable=False, size=(1.45, 0.95),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    democlick2 = event.Mouse(win=win)
    x, y = [None, None]
    democlick2.mouseClock = core.Clock()
    textbox_2 = visual.TextBox2(
         win, text='Try clicking Waldo.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.4), draggable=False,      letterHeight=0.05,
         size=(0.4, 0.4), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_2',
         depth=-2, autoLog=True,
    )
    
    # --- Initialize components for Routine "correctsound" ---
    correctSound = sound.Sound(
        'A', 
        secs=2.0, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='correctSound'
    )
    correctSound.setVolume(1.0)
    
    # --- Initialize components for Routine "start" ---
    star = visual.ShapeStim(
        win=win, name='star', vertices='star7',
        size=(0.035, 0.035),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=(1.0000, 0.9216, 0.8667), fillColor=(1.0000, 0.9216, 0.8667),
        opacity=None, depth=0.0, interpolate=True)
    start_mouse = event.Mouse(win=win)
    x, y = [None, None]
    start_mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial2" ---
    target2 = visual.ImageStim(
        win=win,
        name='target2', 
        image='stimuli/waldo1.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.175, 0.125),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    trial_mouse2 = event.Mouse(win=win)
    x, y = [None, None]
    trial_mouse2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "correctsound" ---
    correctSound = sound.Sound(
        'A', 
        secs=2.0, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='correctSound'
    )
    correctSound.setVolume(1.0)
    
    # --- Initialize components for Routine "instructions2" ---
    pinkcandycaneinstructions = visual.TextBox2(
         win, text='Fantastic!\n\nNow find the PINK candy cane hidden among the red candy canes.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='pinkcandycaneinstructions',
         depth=0, autoLog=True,
    )
    
    # --- Initialize components for Routine "pinkcandydemo" ---
    demo3 = visual.ImageStim(
        win=win,
        name='demo3', 
        image='stimuli/pinkcandycane.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.10), draggable=False, size=(0.6, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    democlick3 = event.Mouse(win=win)
    x, y = [None, None]
    democlick3.mouseClock = core.Clock()
    demoinstructions3 = visual.TextBox2(
         win, text='Try clicking the candy cane.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0.4), draggable=False,      letterHeight=0.05,
         size=(0.4, 0.4), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='demoinstructions3',
         depth=-2, autoLog=True,
    )
    
    # --- Initialize components for Routine "correctsound" ---
    correctSound = sound.Sound(
        'A', 
        secs=2.0, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='correctSound'
    )
    correctSound.setVolume(1.0)
    
    # --- Initialize components for Routine "start" ---
    star = visual.ShapeStim(
        win=win, name='star', vertices='star7',
        size=(0.035, 0.035),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=(1.0000, 0.9216, 0.8667), fillColor=(1.0000, 0.9216, 0.8667),
        opacity=None, depth=0.0, interpolate=True)
    start_mouse = event.Mouse(win=win)
    x, y = [None, None]
    start_mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial3" ---
    target3 = visual.ImageStim(
        win=win,
        name='target3', 
        image='stimuli/pinkcandycane.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    trial_mouse3 = event.Mouse(win=win)
    x, y = [None, None]
    trial_mouse3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "correctsound" ---
    correctSound = sound.Sound(
        'A', 
        secs=2.0, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='correctSound'
    )
    correctSound.setVolume(1.0)
    
    # --- Initialize components for Routine "resultsscreen" ---
    thanks = visual.TextBox2(
         win, text='Thank you for participating in this experiment.', placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, 0), draggable=False,      letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='thanks',
         depth=0, autoLog=True,
    )
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instructions0" ---
    # create an object to store info about Routine instructions0
    instructions0 = data.Routine(
        name='instructions0',
        components=[textbox],
    )
    instructions0.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    textbox.reset()
    # store start times for instructions0
    instructions0.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions0.tStart = globalClock.getTime(format='float')
    instructions0.status = STARTED
    thisExp.addData('instructions0.started', instructions0.tStart)
    instructions0.maxDuration = None
    # keep track of which components have finished
    instructions0Components = instructions0.components
    for thisComponent in instructions0.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions0" ---
    thisExp.currentRoutine = instructions0
    instructions0.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textbox* updates
        
        # if textbox is starting this frame...
        if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox.frameNStart = frameN  # exact frame index
            textbox.tStart = t  # local t and not account for scr refresh
            textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox.started')
            # update status
            textbox.status = STARTED
            textbox.setAutoDraw(True)
        
        # if textbox is active this frame...
        if textbox.status == STARTED:
            # update params
            pass
        
        # if textbox is stopping this frame...
        if textbox.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                textbox.tStop = t  # not accounting for scr refresh
                textbox.tStopRefresh = tThisFlipGlobal  # on global time
                textbox.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox.stopped')
                # update status
                textbox.status = FINISHED
                textbox.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions0,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions0.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions0.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions0.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions0" ---
    for thisComponent in instructions0.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions0
    instructions0.tStop = globalClock.getTime(format='float')
    instructions0.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions0.stopped', instructions0.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if instructions0.maxDurationReached:
        routineTimer.addTime(-instructions0.maxDuration)
    elif instructions0.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "waldodemo1" ---
    # create an object to store info about Routine waldodemo1
    waldodemo1 = data.Routine(
        name='waldodemo1',
        components=[demo1, democlick1, demoinstructions1],
    )
    waldodemo1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the democlick1
    democlick1.x = []
    democlick1.y = []
    democlick1.leftButton = []
    democlick1.midButton = []
    democlick1.rightButton = []
    democlick1.time = []
    democlick1.clicked_name = []
    gotValidClick = False  # until a click is received
    demoinstructions1.reset()
    # store start times for waldodemo1
    waldodemo1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    waldodemo1.tStart = globalClock.getTime(format='float')
    waldodemo1.status = STARTED
    thisExp.addData('waldodemo1.started', waldodemo1.tStart)
    waldodemo1.maxDuration = None
    # keep track of which components have finished
    waldodemo1Components = waldodemo1.components
    for thisComponent in waldodemo1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "waldodemo1" ---
    thisExp.currentRoutine = waldodemo1
    waldodemo1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *demo1* updates
        
        # if demo1 is starting this frame...
        if demo1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demo1.frameNStart = frameN  # exact frame index
            demo1.tStart = t  # local t and not account for scr refresh
            demo1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demo1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'demo1.started')
            # update status
            demo1.status = STARTED
            demo1.setAutoDraw(True)
        
        # if demo1 is active this frame...
        if demo1.status == STARTED:
            # update params
            pass
        # *democlick1* updates
        
        # if democlick1 is starting this frame...
        if democlick1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            democlick1.frameNStart = frameN  # exact frame index
            democlick1.tStart = t  # local t and not account for scr refresh
            democlick1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(democlick1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('democlick1.started', t)
            # update status
            democlick1.status = STARTED
            democlick1.mouseClock.reset()
            prevButtonState = democlick1.getPressed()  # if button is down already this ISN'T a new click
        if democlick1.status == STARTED:  # only update if started and not finished!
            buttons = democlick1.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(demo1, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(democlick1):
                            gotValidClick = True
                            democlick1.clicked_name.append(obj.name)
                    if not gotValidClick:
                        democlick1.clicked_name.append(None)
                    x, y = democlick1.getPos()
                    democlick1.x.append(float(x))
                    democlick1.y.append(float(y))
                    buttons = democlick1.getPressed()
                    democlick1.leftButton.append(buttons[0])
                    democlick1.midButton.append(buttons[1])
                    democlick1.rightButton.append(buttons[2])
                    democlick1.time.append(democlick1.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *demoinstructions1* updates
        
        # if demoinstructions1 is starting this frame...
        if demoinstructions1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demoinstructions1.frameNStart = frameN  # exact frame index
            demoinstructions1.tStart = t  # local t and not account for scr refresh
            demoinstructions1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demoinstructions1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'demoinstructions1.started')
            # update status
            demoinstructions1.status = STARTED
            demoinstructions1.setAutoDraw(True)
        
        # if demoinstructions1 is active this frame...
        if demoinstructions1.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=waldodemo1,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            waldodemo1.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if waldodemo1.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in waldodemo1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "waldodemo1" ---
    for thisComponent in waldodemo1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for waldodemo1
    waldodemo1.tStop = globalClock.getTime(format='float')
    waldodemo1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('waldodemo1.stopped', waldodemo1.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('democlick1.x', democlick1.x)
    thisExp.addData('democlick1.y', democlick1.y)
    thisExp.addData('democlick1.leftButton', democlick1.leftButton)
    thisExp.addData('democlick1.midButton', democlick1.midButton)
    thisExp.addData('democlick1.rightButton', democlick1.rightButton)
    thisExp.addData('democlick1.time', democlick1.time)
    thisExp.addData('democlick1.clicked_name', democlick1.clicked_name)
    thisExp.nextEntry()
    # the Routine "waldodemo1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "correctsound" ---
    # create an object to store info about Routine correctsound
    correctsound = data.Routine(
        name='correctsound',
        components=[correctSound],
    )
    correctsound.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    correctSound.setSound('stimuli/correct.wav', secs=2.0, hamming=True)
    correctSound.setVolume(1.0, log=False)
    correctSound.seek(0)
    # store start times for correctsound
    correctsound.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    correctsound.tStart = globalClock.getTime(format='float')
    correctsound.status = STARTED
    thisExp.addData('correctsound.started', correctsound.tStart)
    correctsound.maxDuration = None
    # keep track of which components have finished
    correctsoundComponents = correctsound.components
    for thisComponent in correctsound.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "correctsound" ---
    thisExp.currentRoutine = correctsound
    correctsound.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *correctSound* updates
        
        # if correctSound is starting this frame...
        if correctSound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            correctSound.frameNStart = frameN  # exact frame index
            correctSound.tStart = t  # local t and not account for scr refresh
            correctSound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('correctSound.started', tThisFlipGlobal)
            # update status
            correctSound.status = STARTED
            correctSound.play(when=win)  # sync with win flip
        
        # if correctSound is stopping this frame...
        if correctSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correctSound.tStartRefresh + 2.0-frameTolerance or correctSound.isFinished:
                # keep track of stop time/frame for later
                correctSound.tStop = t  # not accounting for scr refresh
                correctSound.tStopRefresh = tThisFlipGlobal  # on global time
                correctSound.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'correctSound.stopped')
                # update status
                correctSound.status = FINISHED
                correctSound.stop()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=correctsound,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            correctsound.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if correctsound.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in correctsound.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "correctsound" ---
    for thisComponent in correctsound.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for correctsound
    correctsound.tStop = globalClock.getTime(format='float')
    correctsound.tStopRefresh = tThisFlipGlobal
    thisExp.addData('correctsound.stopped', correctsound.tStop)
    correctSound.pause()  # ensure sound has stopped at end of Routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if correctsound.maxDurationReached:
        routineTimer.addTime(-correctsound.maxDuration)
    elif correctsound.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "clickthestar" ---
    # create an object to store info about Routine clickthestar
    clickthestar = data.Routine(
        name='clickthestar',
        components=[clickstar],
    )
    clickthestar.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    clickstar.reset()
    # store start times for clickthestar
    clickthestar.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    clickthestar.tStart = globalClock.getTime(format='float')
    clickthestar.status = STARTED
    thisExp.addData('clickthestar.started', clickthestar.tStart)
    clickthestar.maxDuration = None
    # keep track of which components have finished
    clickthestarComponents = clickthestar.components
    for thisComponent in clickthestar.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "clickthestar" ---
    thisExp.currentRoutine = clickthestar
    clickthestar.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *clickstar* updates
        
        # if clickstar is starting this frame...
        if clickstar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clickstar.frameNStart = frameN  # exact frame index
            clickstar.tStart = t  # local t and not account for scr refresh
            clickstar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clickstar, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'clickstar.started')
            # update status
            clickstar.status = STARTED
            clickstar.setAutoDraw(True)
        
        # if clickstar is active this frame...
        if clickstar.status == STARTED:
            # update params
            pass
        
        # if clickstar is stopping this frame...
        if clickstar.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clickstar.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                clickstar.tStop = t  # not accounting for scr refresh
                clickstar.tStopRefresh = tThisFlipGlobal  # on global time
                clickstar.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'clickstar.stopped')
                # update status
                clickstar.status = FINISHED
                clickstar.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=clickthestar,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            clickthestar.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if clickthestar.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in clickthestar.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "clickthestar" ---
    for thisComponent in clickthestar.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for clickthestar
    clickthestar.tStop = globalClock.getTime(format='float')
    clickthestar.tStopRefresh = tThisFlipGlobal
    thisExp.addData('clickthestar.stopped', clickthestar.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if clickthestar.maxDurationReached:
        routineTimer.addTime(-clickthestar.maxDuration)
    elif clickthestar.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=10, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "start" ---
        # create an object to store info about Routine start
        start = data.Routine(
            name='start',
            components=[star, start_mouse],
        )
        start.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the start_mouse
        start_mouse.x = []
        start_mouse.y = []
        start_mouse.leftButton = []
        start_mouse.midButton = []
        start_mouse.rightButton = []
        start_mouse.time = []
        start_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for start
        start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        start.tStart = globalClock.getTime(format='float')
        start.status = STARTED
        thisExp.addData('start.started', start.tStart)
        start.maxDuration = None
        # keep track of which components have finished
        startComponents = start.components
        for thisComponent in start.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start" ---
        thisExp.currentRoutine = start
        start.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *star* updates
            
            # if star is starting this frame...
            if star.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                star.frameNStart = frameN  # exact frame index
                star.tStart = t  # local t and not account for scr refresh
                star.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'star.started')
                # update status
                star.status = STARTED
                star.setAutoDraw(True)
            
            # if star is active this frame...
            if star.status == STARTED:
                # update params
                pass
            # *start_mouse* updates
            
            # if start_mouse is starting this frame...
            if start_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_mouse.frameNStart = frameN  # exact frame index
                start_mouse.tStart = t  # local t and not account for scr refresh
                start_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('start_mouse.started', t)
                # update status
                start_mouse.status = STARTED
                start_mouse.mouseClock.reset()
                prevButtonState = start_mouse.getPressed()  # if button is down already this ISN'T a new click
            if start_mouse.status == STARTED:  # only update if started and not finished!
                buttons = start_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(star, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(start_mouse):
                                gotValidClick = True
                                start_mouse.clicked_name.append(obj.name)
                        if not gotValidClick:
                            start_mouse.clicked_name.append(None)
                        x, y = start_mouse.getPos()
                        start_mouse.x.append(float(x))
                        start_mouse.y.append(float(y))
                        buttons = start_mouse.getPressed()
                        start_mouse.leftButton.append(buttons[0])
                        start_mouse.midButton.append(buttons[1])
                        start_mouse.rightButton.append(buttons[2])
                        start_mouse.time.append(start_mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=start,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                start.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if start.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in start.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start" ---
        for thisComponent in start.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for start
        start.tStop = globalClock.getTime(format='float')
        start.tStopRefresh = tThisFlipGlobal
        thisExp.addData('start.stopped', start.tStop)
        # store data for trials (TrialHandler)
        trials.addData('start_mouse.x', start_mouse.x)
        trials.addData('start_mouse.y', start_mouse.y)
        trials.addData('start_mouse.leftButton', start_mouse.leftButton)
        trials.addData('start_mouse.midButton', start_mouse.midButton)
        trials.addData('start_mouse.rightButton', start_mouse.rightButton)
        trials.addData('start_mouse.time', start_mouse.time)
        trials.addData('start_mouse.clicked_name', start_mouse.clicked_name)
        # the Routine "start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial1" ---
        # create an object to store info about Routine trial1
        trial1 = data.Routine(
            name='trial1',
            components=[target1, trial_mouse],
        )
        trial1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        target1.setPos((random()-0.5, random()-0.5))
        # setup some python lists for storing info about the trial_mouse
        trial_mouse.x = []
        trial_mouse.y = []
        trial_mouse.leftButton = []
        trial_mouse.midButton = []
        trial_mouse.rightButton = []
        trial_mouse.time = []
        trial_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code1
        import random as rnd
        
        false_images = []
        
        trial_mouse.clickReset()
        trial_mouse.setPos((0, 0))
        
        mouseReleased = False
        
        for i in range(150):
            pos = (rnd.uniform(-0.5, 0.5), rnd.uniform(-0.5, 0.5))
        
            stim = visual.ImageStim(
                win=win,
                image='stimuli/candycane.png',
                pos=pos,
                size=(0.1, 0.1)
            )
            false_images.append(stim)
        # store start times for trial1
        trial1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial1.tStart = globalClock.getTime(format='float')
        trial1.status = STARTED
        thisExp.addData('trial1.started', trial1.tStart)
        trial1.maxDuration = None
        # keep track of which components have finished
        trial1Components = trial1.components
        for thisComponent in trial1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial1" ---
        thisExp.currentRoutine = trial1
        trial1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *target1* updates
            
            # if target1 is starting this frame...
            if target1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target1.frameNStart = frameN  # exact frame index
                target1.tStart = t  # local t and not account for scr refresh
                target1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target1.started')
                # update status
                target1.status = STARTED
                target1.setAutoDraw(True)
            
            # if target1 is active this frame...
            if target1.status == STARTED:
                # update params
                pass
            # *trial_mouse* updates
            
            # if trial_mouse is starting this frame...
            if trial_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_mouse.frameNStart = frameN  # exact frame index
                trial_mouse.tStart = t  # local t and not account for scr refresh
                trial_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('trial_mouse.started', t)
                # update status
                trial_mouse.status = STARTED
                trial_mouse.mouseClock.reset()
                prevButtonState = trial_mouse.getPressed()  # if button is down already this ISN'T a new click
            if trial_mouse.status == STARTED:  # only update if started and not finished!
                buttons = trial_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(target1, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(trial_mouse):
                                gotValidClick = True
                                trial_mouse.clicked_name.append(obj.name)
                        if not gotValidClick:
                            trial_mouse.clicked_name.append(None)
                        x, y = trial_mouse.getPos()
                        trial_mouse.x.append(float(x))
                        trial_mouse.y.append(float(y))
                        buttons = trial_mouse.getPressed()
                        trial_mouse.leftButton.append(buttons[0])
                        trial_mouse.midButton.append(buttons[1])
                        trial_mouse.rightButton.append(buttons[2])
                        trial_mouse.time.append(trial_mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            # Run 'Each Frame' code from code1
            for stim in false_images:
                stim.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial1,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trial1.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trial1.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trial1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial1" ---
        for thisComponent in trial1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial1
        trial1.tStop = globalClock.getTime(format='float')
        trial1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial1.stopped', trial1.tStop)
        # store data for trials (TrialHandler)
        trials.addData('trial_mouse.x', trial_mouse.x)
        trials.addData('trial_mouse.y', trial_mouse.y)
        trials.addData('trial_mouse.leftButton', trial_mouse.leftButton)
        trials.addData('trial_mouse.midButton', trial_mouse.midButton)
        trials.addData('trial_mouse.rightButton', trial_mouse.rightButton)
        trials.addData('trial_mouse.time', trial_mouse.time)
        trials.addData('trial_mouse.clicked_name', trial_mouse.clicked_name)
        # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "correctsound" ---
        # create an object to store info about Routine correctsound
        correctsound = data.Routine(
            name='correctsound',
            components=[correctSound],
        )
        correctsound.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        correctSound.setSound('stimuli/correct.wav', secs=2.0, hamming=True)
        correctSound.setVolume(1.0, log=False)
        correctSound.seek(0)
        # store start times for correctsound
        correctsound.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        correctsound.tStart = globalClock.getTime(format='float')
        correctsound.status = STARTED
        thisExp.addData('correctsound.started', correctsound.tStart)
        correctsound.maxDuration = None
        # keep track of which components have finished
        correctsoundComponents = correctsound.components
        for thisComponent in correctsound.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "correctsound" ---
        thisExp.currentRoutine = correctsound
        correctsound.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *correctSound* updates
            
            # if correctSound is starting this frame...
            if correctSound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                correctSound.frameNStart = frameN  # exact frame index
                correctSound.tStart = t  # local t and not account for scr refresh
                correctSound.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('correctSound.started', tThisFlipGlobal)
                # update status
                correctSound.status = STARTED
                correctSound.play(when=win)  # sync with win flip
            
            # if correctSound is stopping this frame...
            if correctSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > correctSound.tStartRefresh + 2.0-frameTolerance or correctSound.isFinished:
                    # keep track of stop time/frame for later
                    correctSound.tStop = t  # not accounting for scr refresh
                    correctSound.tStopRefresh = tThisFlipGlobal  # on global time
                    correctSound.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'correctSound.stopped')
                    # update status
                    correctSound.status = FINISHED
                    correctSound.stop()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=correctsound,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                correctsound.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if correctsound.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in correctsound.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "correctsound" ---
        for thisComponent in correctsound.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for correctsound
        correctsound.tStop = globalClock.getTime(format='float')
        correctsound.tStopRefresh = tThisFlipGlobal
        thisExp.addData('correctsound.stopped', correctsound.tStop)
        correctSound.pause()  # ensure sound has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if correctsound.maxDurationReached:
            routineTimer.addTime(-correctsound.maxDuration)
        elif correctsound.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 10 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instructions1" ---
    # create an object to store info about Routine instructions1
    instructions1 = data.Routine(
        name='instructions1',
        components=[secondtrial],
    )
    instructions1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    secondtrial.reset()
    # store start times for instructions1
    instructions1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions1.tStart = globalClock.getTime(format='float')
    instructions1.status = STARTED
    thisExp.addData('instructions1.started', instructions1.tStart)
    instructions1.maxDuration = None
    # keep track of which components have finished
    instructions1Components = instructions1.components
    for thisComponent in instructions1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions1" ---
    thisExp.currentRoutine = instructions1
    instructions1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *secondtrial* updates
        
        # if secondtrial is starting this frame...
        if secondtrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            secondtrial.frameNStart = frameN  # exact frame index
            secondtrial.tStart = t  # local t and not account for scr refresh
            secondtrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(secondtrial, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'secondtrial.started')
            # update status
            secondtrial.status = STARTED
            secondtrial.setAutoDraw(True)
        
        # if secondtrial is active this frame...
        if secondtrial.status == STARTED:
            # update params
            pass
        
        # if secondtrial is stopping this frame...
        if secondtrial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > secondtrial.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                secondtrial.tStop = t  # not accounting for scr refresh
                secondtrial.tStopRefresh = tThisFlipGlobal  # on global time
                secondtrial.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'secondtrial.stopped')
                # update status
                secondtrial.status = FINISHED
                secondtrial.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions1,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions1.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions1.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions1" ---
    for thisComponent in instructions1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions1
    instructions1.tStop = globalClock.getTime(format='float')
    instructions1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions1.stopped', instructions1.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if instructions1.maxDurationReached:
        routineTimer.addTime(-instructions1.maxDuration)
    elif instructions1.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "waldodemo2" ---
    # create an object to store info about Routine waldodemo2
    waldodemo2 = data.Routine(
        name='waldodemo2',
        components=[demo2, democlick2, textbox_2],
    )
    waldodemo2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the democlick2
    democlick2.x = []
    democlick2.y = []
    democlick2.leftButton = []
    democlick2.midButton = []
    democlick2.rightButton = []
    democlick2.time = []
    democlick2.clicked_name = []
    gotValidClick = False  # until a click is received
    textbox_2.reset()
    # store start times for waldodemo2
    waldodemo2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    waldodemo2.tStart = globalClock.getTime(format='float')
    waldodemo2.status = STARTED
    thisExp.addData('waldodemo2.started', waldodemo2.tStart)
    waldodemo2.maxDuration = None
    # keep track of which components have finished
    waldodemo2Components = waldodemo2.components
    for thisComponent in waldodemo2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "waldodemo2" ---
    thisExp.currentRoutine = waldodemo2
    waldodemo2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *demo2* updates
        
        # if demo2 is starting this frame...
        if demo2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demo2.frameNStart = frameN  # exact frame index
            demo2.tStart = t  # local t and not account for scr refresh
            demo2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demo2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'demo2.started')
            # update status
            demo2.status = STARTED
            demo2.setAutoDraw(True)
        
        # if demo2 is active this frame...
        if demo2.status == STARTED:
            # update params
            pass
        # *democlick2* updates
        
        # if democlick2 is starting this frame...
        if democlick2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            democlick2.frameNStart = frameN  # exact frame index
            democlick2.tStart = t  # local t and not account for scr refresh
            democlick2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(democlick2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('democlick2.started', t)
            # update status
            democlick2.status = STARTED
            democlick2.mouseClock.reset()
            prevButtonState = democlick2.getPressed()  # if button is down already this ISN'T a new click
        if democlick2.status == STARTED:  # only update if started and not finished!
            buttons = democlick2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(demo2, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(democlick2):
                            gotValidClick = True
                            democlick2.clicked_name.append(obj.name)
                    if not gotValidClick:
                        democlick2.clicked_name.append(None)
                    x, y = democlick2.getPos()
                    democlick2.x.append(float(x))
                    democlick2.y.append(float(y))
                    buttons = democlick2.getPressed()
                    democlick2.leftButton.append(buttons[0])
                    democlick2.midButton.append(buttons[1])
                    democlick2.rightButton.append(buttons[2])
                    democlick2.time.append(democlick2.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *textbox_2* updates
        
        # if textbox_2 is starting this frame...
        if textbox_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_2.frameNStart = frameN  # exact frame index
            textbox_2.tStart = t  # local t and not account for scr refresh
            textbox_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox_2.started')
            # update status
            textbox_2.status = STARTED
            textbox_2.setAutoDraw(True)
        
        # if textbox_2 is active this frame...
        if textbox_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=waldodemo2,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            waldodemo2.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if waldodemo2.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in waldodemo2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "waldodemo2" ---
    for thisComponent in waldodemo2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for waldodemo2
    waldodemo2.tStop = globalClock.getTime(format='float')
    waldodemo2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('waldodemo2.stopped', waldodemo2.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('democlick2.x', democlick2.x)
    thisExp.addData('democlick2.y', democlick2.y)
    thisExp.addData('democlick2.leftButton', democlick2.leftButton)
    thisExp.addData('democlick2.midButton', democlick2.midButton)
    thisExp.addData('democlick2.rightButton', democlick2.rightButton)
    thisExp.addData('democlick2.time', democlick2.time)
    thisExp.addData('democlick2.clicked_name', democlick2.clicked_name)
    thisExp.nextEntry()
    # the Routine "waldodemo2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "correctsound" ---
    # create an object to store info about Routine correctsound
    correctsound = data.Routine(
        name='correctsound',
        components=[correctSound],
    )
    correctsound.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    correctSound.setSound('stimuli/correct.wav', secs=2.0, hamming=True)
    correctSound.setVolume(1.0, log=False)
    correctSound.seek(0)
    # store start times for correctsound
    correctsound.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    correctsound.tStart = globalClock.getTime(format='float')
    correctsound.status = STARTED
    thisExp.addData('correctsound.started', correctsound.tStart)
    correctsound.maxDuration = None
    # keep track of which components have finished
    correctsoundComponents = correctsound.components
    for thisComponent in correctsound.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "correctsound" ---
    thisExp.currentRoutine = correctsound
    correctsound.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *correctSound* updates
        
        # if correctSound is starting this frame...
        if correctSound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            correctSound.frameNStart = frameN  # exact frame index
            correctSound.tStart = t  # local t and not account for scr refresh
            correctSound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('correctSound.started', tThisFlipGlobal)
            # update status
            correctSound.status = STARTED
            correctSound.play(when=win)  # sync with win flip
        
        # if correctSound is stopping this frame...
        if correctSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correctSound.tStartRefresh + 2.0-frameTolerance or correctSound.isFinished:
                # keep track of stop time/frame for later
                correctSound.tStop = t  # not accounting for scr refresh
                correctSound.tStopRefresh = tThisFlipGlobal  # on global time
                correctSound.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'correctSound.stopped')
                # update status
                correctSound.status = FINISHED
                correctSound.stop()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=correctsound,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            correctsound.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if correctsound.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in correctsound.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "correctsound" ---
    for thisComponent in correctsound.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for correctsound
    correctsound.tStop = globalClock.getTime(format='float')
    correctsound.tStopRefresh = tThisFlipGlobal
    thisExp.addData('correctsound.stopped', correctsound.tStop)
    correctSound.pause()  # ensure sound has stopped at end of Routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if correctsound.maxDurationReached:
        routineTimer.addTime(-correctsound.maxDuration)
    elif correctsound.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler2(
        name='trials_2',
        nReps=10, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            globals()[paramName] = thisTrial_2[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_2 in trials_2:
        trials_2.status = STARTED
        if hasattr(thisTrial_2, 'status'):
            thisTrial_2.status = STARTED
        currentLoop = trials_2
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        # --- Prepare to start Routine "start" ---
        # create an object to store info about Routine start
        start = data.Routine(
            name='start',
            components=[star, start_mouse],
        )
        start.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the start_mouse
        start_mouse.x = []
        start_mouse.y = []
        start_mouse.leftButton = []
        start_mouse.midButton = []
        start_mouse.rightButton = []
        start_mouse.time = []
        start_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for start
        start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        start.tStart = globalClock.getTime(format='float')
        start.status = STARTED
        thisExp.addData('start.started', start.tStart)
        start.maxDuration = None
        # keep track of which components have finished
        startComponents = start.components
        for thisComponent in start.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start" ---
        thisExp.currentRoutine = start
        start.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_2, 'status') and thisTrial_2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *star* updates
            
            # if star is starting this frame...
            if star.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                star.frameNStart = frameN  # exact frame index
                star.tStart = t  # local t and not account for scr refresh
                star.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'star.started')
                # update status
                star.status = STARTED
                star.setAutoDraw(True)
            
            # if star is active this frame...
            if star.status == STARTED:
                # update params
                pass
            # *start_mouse* updates
            
            # if start_mouse is starting this frame...
            if start_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_mouse.frameNStart = frameN  # exact frame index
                start_mouse.tStart = t  # local t and not account for scr refresh
                start_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('start_mouse.started', t)
                # update status
                start_mouse.status = STARTED
                start_mouse.mouseClock.reset()
                prevButtonState = start_mouse.getPressed()  # if button is down already this ISN'T a new click
            if start_mouse.status == STARTED:  # only update if started and not finished!
                buttons = start_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(star, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(start_mouse):
                                gotValidClick = True
                                start_mouse.clicked_name.append(obj.name)
                        if not gotValidClick:
                            start_mouse.clicked_name.append(None)
                        x, y = start_mouse.getPos()
                        start_mouse.x.append(float(x))
                        start_mouse.y.append(float(y))
                        buttons = start_mouse.getPressed()
                        start_mouse.leftButton.append(buttons[0])
                        start_mouse.midButton.append(buttons[1])
                        start_mouse.rightButton.append(buttons[2])
                        start_mouse.time.append(start_mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=start,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                start.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if start.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in start.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start" ---
        for thisComponent in start.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for start
        start.tStop = globalClock.getTime(format='float')
        start.tStopRefresh = tThisFlipGlobal
        thisExp.addData('start.stopped', start.tStop)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('start_mouse.x', start_mouse.x)
        trials_2.addData('start_mouse.y', start_mouse.y)
        trials_2.addData('start_mouse.leftButton', start_mouse.leftButton)
        trials_2.addData('start_mouse.midButton', start_mouse.midButton)
        trials_2.addData('start_mouse.rightButton', start_mouse.rightButton)
        trials_2.addData('start_mouse.time', start_mouse.time)
        trials_2.addData('start_mouse.clicked_name', start_mouse.clicked_name)
        # the Routine "start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial2" ---
        # create an object to store info about Routine trial2
        trial2 = data.Routine(
            name='trial2',
            components=[target2, trial_mouse2],
        )
        trial2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        target2.setPos((random()-0.5, random()-0.5))
        # setup some python lists for storing info about the trial_mouse2
        trial_mouse2.x = []
        trial_mouse2.y = []
        trial_mouse2.leftButton = []
        trial_mouse2.midButton = []
        trial_mouse2.rightButton = []
        trial_mouse2.time = []
        trial_mouse2.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code2
        import random as rnd
        
        false_images = []
        
        trial_mouse.clickReset()
        trial_mouse.setPos((0, 0))
        
        mouseReleased = False
        
        for i in range(150):
            pos = (rnd.uniform(-0.5, 0.5), rnd.uniform(-0.5, 0.5))
        
            stim = visual.ImageStim(
                win=win,
                image='stimuli/candycane.png',
                pos=pos,
                size=(0.1, 0.1)
            )
            false_images.append(stim)
        # store start times for trial2
        trial2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial2.tStart = globalClock.getTime(format='float')
        trial2.status = STARTED
        thisExp.addData('trial2.started', trial2.tStart)
        trial2.maxDuration = None
        # keep track of which components have finished
        trial2Components = trial2.components
        for thisComponent in trial2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial2" ---
        thisExp.currentRoutine = trial2
        trial2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_2, 'status') and thisTrial_2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *target2* updates
            
            # if target2 is starting this frame...
            if target2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target2.frameNStart = frameN  # exact frame index
                target2.tStart = t  # local t and not account for scr refresh
                target2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2.started')
                # update status
                target2.status = STARTED
                target2.setAutoDraw(True)
            
            # if target2 is active this frame...
            if target2.status == STARTED:
                # update params
                pass
            # *trial_mouse2* updates
            
            # if trial_mouse2 is starting this frame...
            if trial_mouse2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_mouse2.frameNStart = frameN  # exact frame index
                trial_mouse2.tStart = t  # local t and not account for scr refresh
                trial_mouse2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_mouse2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('trial_mouse2.started', t)
                # update status
                trial_mouse2.status = STARTED
                trial_mouse2.mouseClock.reset()
                prevButtonState = trial_mouse2.getPressed()  # if button is down already this ISN'T a new click
            if trial_mouse2.status == STARTED:  # only update if started and not finished!
                buttons = trial_mouse2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(target2, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(trial_mouse2):
                                gotValidClick = True
                                trial_mouse2.clicked_name.append(obj.name)
                        if not gotValidClick:
                            trial_mouse2.clicked_name.append(None)
                        x, y = trial_mouse2.getPos()
                        trial_mouse2.x.append(float(x))
                        trial_mouse2.y.append(float(y))
                        buttons = trial_mouse2.getPressed()
                        trial_mouse2.leftButton.append(buttons[0])
                        trial_mouse2.midButton.append(buttons[1])
                        trial_mouse2.rightButton.append(buttons[2])
                        trial_mouse2.time.append(trial_mouse2.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            # Run 'Each Frame' code from code2
            for stim in false_images:
                stim.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial2,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trial2.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trial2.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trial2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial2" ---
        for thisComponent in trial2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial2
        trial2.tStop = globalClock.getTime(format='float')
        trial2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial2.stopped', trial2.tStop)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('trial_mouse2.x', trial_mouse2.x)
        trials_2.addData('trial_mouse2.y', trial_mouse2.y)
        trials_2.addData('trial_mouse2.leftButton', trial_mouse2.leftButton)
        trials_2.addData('trial_mouse2.midButton', trial_mouse2.midButton)
        trials_2.addData('trial_mouse2.rightButton', trial_mouse2.rightButton)
        trials_2.addData('trial_mouse2.time', trial_mouse2.time)
        trials_2.addData('trial_mouse2.clicked_name', trial_mouse2.clicked_name)
        # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "correctsound" ---
        # create an object to store info about Routine correctsound
        correctsound = data.Routine(
            name='correctsound',
            components=[correctSound],
        )
        correctsound.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        correctSound.setSound('stimuli/correct.wav', secs=2.0, hamming=True)
        correctSound.setVolume(1.0, log=False)
        correctSound.seek(0)
        # store start times for correctsound
        correctsound.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        correctsound.tStart = globalClock.getTime(format='float')
        correctsound.status = STARTED
        thisExp.addData('correctsound.started', correctsound.tStart)
        correctsound.maxDuration = None
        # keep track of which components have finished
        correctsoundComponents = correctsound.components
        for thisComponent in correctsound.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "correctsound" ---
        thisExp.currentRoutine = correctsound
        correctsound.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_2, 'status') and thisTrial_2.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *correctSound* updates
            
            # if correctSound is starting this frame...
            if correctSound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                correctSound.frameNStart = frameN  # exact frame index
                correctSound.tStart = t  # local t and not account for scr refresh
                correctSound.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('correctSound.started', tThisFlipGlobal)
                # update status
                correctSound.status = STARTED
                correctSound.play(when=win)  # sync with win flip
            
            # if correctSound is stopping this frame...
            if correctSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > correctSound.tStartRefresh + 2.0-frameTolerance or correctSound.isFinished:
                    # keep track of stop time/frame for later
                    correctSound.tStop = t  # not accounting for scr refresh
                    correctSound.tStopRefresh = tThisFlipGlobal  # on global time
                    correctSound.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'correctSound.stopped')
                    # update status
                    correctSound.status = FINISHED
                    correctSound.stop()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=correctsound,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                correctsound.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if correctsound.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in correctsound.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "correctsound" ---
        for thisComponent in correctsound.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for correctsound
        correctsound.tStop = globalClock.getTime(format='float')
        correctsound.tStopRefresh = tThisFlipGlobal
        thisExp.addData('correctsound.stopped', correctsound.tStop)
        correctSound.pause()  # ensure sound has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if correctsound.maxDurationReached:
            routineTimer.addTime(-correctsound.maxDuration)
        elif correctsound.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisTrial_2 as finished
        if hasattr(thisTrial_2, 'status'):
            thisTrial_2.status = FINISHED
        # if awaiting a pause, pause now
        if trials_2.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_2.status = STARTED
        thisExp.nextEntry()
        
    # completed 10 repeats of 'trials_2'
    trials_2.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instructions2" ---
    # create an object to store info about Routine instructions2
    instructions2 = data.Routine(
        name='instructions2',
        components=[pinkcandycaneinstructions],
    )
    instructions2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    pinkcandycaneinstructions.reset()
    # store start times for instructions2
    instructions2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions2.tStart = globalClock.getTime(format='float')
    instructions2.status = STARTED
    thisExp.addData('instructions2.started', instructions2.tStart)
    instructions2.maxDuration = None
    # keep track of which components have finished
    instructions2Components = instructions2.components
    for thisComponent in instructions2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions2" ---
    thisExp.currentRoutine = instructions2
    instructions2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pinkcandycaneinstructions* updates
        
        # if pinkcandycaneinstructions is starting this frame...
        if pinkcandycaneinstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pinkcandycaneinstructions.frameNStart = frameN  # exact frame index
            pinkcandycaneinstructions.tStart = t  # local t and not account for scr refresh
            pinkcandycaneinstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pinkcandycaneinstructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'pinkcandycaneinstructions.started')
            # update status
            pinkcandycaneinstructions.status = STARTED
            pinkcandycaneinstructions.setAutoDraw(True)
        
        # if pinkcandycaneinstructions is active this frame...
        if pinkcandycaneinstructions.status == STARTED:
            # update params
            pass
        
        # if pinkcandycaneinstructions is stopping this frame...
        if pinkcandycaneinstructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pinkcandycaneinstructions.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                pinkcandycaneinstructions.tStop = t  # not accounting for scr refresh
                pinkcandycaneinstructions.tStopRefresh = tThisFlipGlobal  # on global time
                pinkcandycaneinstructions.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pinkcandycaneinstructions.stopped')
                # update status
                pinkcandycaneinstructions.status = FINISHED
                pinkcandycaneinstructions.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions2,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions2.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions2.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions2" ---
    for thisComponent in instructions2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions2
    instructions2.tStop = globalClock.getTime(format='float')
    instructions2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions2.stopped', instructions2.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if instructions2.maxDurationReached:
        routineTimer.addTime(-instructions2.maxDuration)
    elif instructions2.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "pinkcandydemo" ---
    # create an object to store info about Routine pinkcandydemo
    pinkcandydemo = data.Routine(
        name='pinkcandydemo',
        components=[demo3, democlick3, demoinstructions3],
    )
    pinkcandydemo.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the democlick3
    democlick3.x = []
    democlick3.y = []
    democlick3.leftButton = []
    democlick3.midButton = []
    democlick3.rightButton = []
    democlick3.time = []
    democlick3.clicked_name = []
    gotValidClick = False  # until a click is received
    demoinstructions3.reset()
    # store start times for pinkcandydemo
    pinkcandydemo.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    pinkcandydemo.tStart = globalClock.getTime(format='float')
    pinkcandydemo.status = STARTED
    thisExp.addData('pinkcandydemo.started', pinkcandydemo.tStart)
    pinkcandydemo.maxDuration = None
    # keep track of which components have finished
    pinkcandydemoComponents = pinkcandydemo.components
    for thisComponent in pinkcandydemo.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "pinkcandydemo" ---
    thisExp.currentRoutine = pinkcandydemo
    pinkcandydemo.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *demo3* updates
        
        # if demo3 is starting this frame...
        if demo3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demo3.frameNStart = frameN  # exact frame index
            demo3.tStart = t  # local t and not account for scr refresh
            demo3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demo3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'demo3.started')
            # update status
            demo3.status = STARTED
            demo3.setAutoDraw(True)
        
        # if demo3 is active this frame...
        if demo3.status == STARTED:
            # update params
            pass
        # *democlick3* updates
        
        # if democlick3 is starting this frame...
        if democlick3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            democlick3.frameNStart = frameN  # exact frame index
            democlick3.tStart = t  # local t and not account for scr refresh
            democlick3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(democlick3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('democlick3.started', t)
            # update status
            democlick3.status = STARTED
            democlick3.mouseClock.reset()
            prevButtonState = democlick3.getPressed()  # if button is down already this ISN'T a new click
        if democlick3.status == STARTED:  # only update if started and not finished!
            buttons = democlick3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(demo3, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(democlick3):
                            gotValidClick = True
                            democlick3.clicked_name.append(obj.name)
                    if not gotValidClick:
                        democlick3.clicked_name.append(None)
                    x, y = democlick3.getPos()
                    democlick3.x.append(float(x))
                    democlick3.y.append(float(y))
                    buttons = democlick3.getPressed()
                    democlick3.leftButton.append(buttons[0])
                    democlick3.midButton.append(buttons[1])
                    democlick3.rightButton.append(buttons[2])
                    democlick3.time.append(democlick3.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *demoinstructions3* updates
        
        # if demoinstructions3 is starting this frame...
        if demoinstructions3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            demoinstructions3.frameNStart = frameN  # exact frame index
            demoinstructions3.tStart = t  # local t and not account for scr refresh
            demoinstructions3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(demoinstructions3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'demoinstructions3.started')
            # update status
            demoinstructions3.status = STARTED
            demoinstructions3.setAutoDraw(True)
        
        # if demoinstructions3 is active this frame...
        if demoinstructions3.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=pinkcandydemo,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            pinkcandydemo.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if pinkcandydemo.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in pinkcandydemo.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pinkcandydemo" ---
    for thisComponent in pinkcandydemo.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for pinkcandydemo
    pinkcandydemo.tStop = globalClock.getTime(format='float')
    pinkcandydemo.tStopRefresh = tThisFlipGlobal
    thisExp.addData('pinkcandydemo.stopped', pinkcandydemo.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('democlick3.x', democlick3.x)
    thisExp.addData('democlick3.y', democlick3.y)
    thisExp.addData('democlick3.leftButton', democlick3.leftButton)
    thisExp.addData('democlick3.midButton', democlick3.midButton)
    thisExp.addData('democlick3.rightButton', democlick3.rightButton)
    thisExp.addData('democlick3.time', democlick3.time)
    thisExp.addData('democlick3.clicked_name', democlick3.clicked_name)
    thisExp.nextEntry()
    # the Routine "pinkcandydemo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "correctsound" ---
    # create an object to store info about Routine correctsound
    correctsound = data.Routine(
        name='correctsound',
        components=[correctSound],
    )
    correctsound.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    correctSound.setSound('stimuli/correct.wav', secs=2.0, hamming=True)
    correctSound.setVolume(1.0, log=False)
    correctSound.seek(0)
    # store start times for correctsound
    correctsound.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    correctsound.tStart = globalClock.getTime(format='float')
    correctsound.status = STARTED
    thisExp.addData('correctsound.started', correctsound.tStart)
    correctsound.maxDuration = None
    # keep track of which components have finished
    correctsoundComponents = correctsound.components
    for thisComponent in correctsound.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "correctsound" ---
    thisExp.currentRoutine = correctsound
    correctsound.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *correctSound* updates
        
        # if correctSound is starting this frame...
        if correctSound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            correctSound.frameNStart = frameN  # exact frame index
            correctSound.tStart = t  # local t and not account for scr refresh
            correctSound.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('correctSound.started', tThisFlipGlobal)
            # update status
            correctSound.status = STARTED
            correctSound.play(when=win)  # sync with win flip
        
        # if correctSound is stopping this frame...
        if correctSound.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > correctSound.tStartRefresh + 2.0-frameTolerance or correctSound.isFinished:
                # keep track of stop time/frame for later
                correctSound.tStop = t  # not accounting for scr refresh
                correctSound.tStopRefresh = tThisFlipGlobal  # on global time
                correctSound.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'correctSound.stopped')
                # update status
                correctSound.status = FINISHED
                correctSound.stop()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=correctsound,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            correctsound.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if correctsound.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in correctsound.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "correctsound" ---
    for thisComponent in correctsound.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for correctsound
    correctsound.tStop = globalClock.getTime(format='float')
    correctsound.tStopRefresh = tThisFlipGlobal
    thisExp.addData('correctsound.stopped', correctsound.tStop)
    correctSound.pause()  # ensure sound has stopped at end of Routine
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if correctsound.maxDurationReached:
        routineTimer.addTime(-correctsound.maxDuration)
    elif correctsound.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler2(
        name='trials_3',
        nReps=10, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials_3)  # add the loop to the experiment
    thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            globals()[paramName] = thisTrial_3[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial_3 in trials_3:
        trials_3.status = STARTED
        if hasattr(thisTrial_3, 'status'):
            thisTrial_3.status = STARTED
        currentLoop = trials_3
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                globals()[paramName] = thisTrial_3[paramName]
        
        # --- Prepare to start Routine "start" ---
        # create an object to store info about Routine start
        start = data.Routine(
            name='start',
            components=[star, start_mouse],
        )
        start.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the start_mouse
        start_mouse.x = []
        start_mouse.y = []
        start_mouse.leftButton = []
        start_mouse.midButton = []
        start_mouse.rightButton = []
        start_mouse.time = []
        start_mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for start
        start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        start.tStart = globalClock.getTime(format='float')
        start.status = STARTED
        thisExp.addData('start.started', start.tStart)
        start.maxDuration = None
        # keep track of which components have finished
        startComponents = start.components
        for thisComponent in start.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "start" ---
        thisExp.currentRoutine = start
        start.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_3, 'status') and thisTrial_3.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *star* updates
            
            # if star is starting this frame...
            if star.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                star.frameNStart = frameN  # exact frame index
                star.tStart = t  # local t and not account for scr refresh
                star.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(star, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'star.started')
                # update status
                star.status = STARTED
                star.setAutoDraw(True)
            
            # if star is active this frame...
            if star.status == STARTED:
                # update params
                pass
            # *start_mouse* updates
            
            # if start_mouse is starting this frame...
            if start_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                start_mouse.frameNStart = frameN  # exact frame index
                start_mouse.tStart = t  # local t and not account for scr refresh
                start_mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(start_mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('start_mouse.started', t)
                # update status
                start_mouse.status = STARTED
                start_mouse.mouseClock.reset()
                prevButtonState = start_mouse.getPressed()  # if button is down already this ISN'T a new click
            if start_mouse.status == STARTED:  # only update if started and not finished!
                buttons = start_mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(star, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(start_mouse):
                                gotValidClick = True
                                start_mouse.clicked_name.append(obj.name)
                        if not gotValidClick:
                            start_mouse.clicked_name.append(None)
                        x, y = start_mouse.getPos()
                        start_mouse.x.append(float(x))
                        start_mouse.y.append(float(y))
                        buttons = start_mouse.getPressed()
                        start_mouse.leftButton.append(buttons[0])
                        start_mouse.midButton.append(buttons[1])
                        start_mouse.rightButton.append(buttons[2])
                        start_mouse.time.append(start_mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=start,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                start.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if start.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in start.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "start" ---
        for thisComponent in start.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for start
        start.tStop = globalClock.getTime(format='float')
        start.tStopRefresh = tThisFlipGlobal
        thisExp.addData('start.stopped', start.tStop)
        # store data for trials_3 (TrialHandler)
        trials_3.addData('start_mouse.x', start_mouse.x)
        trials_3.addData('start_mouse.y', start_mouse.y)
        trials_3.addData('start_mouse.leftButton', start_mouse.leftButton)
        trials_3.addData('start_mouse.midButton', start_mouse.midButton)
        trials_3.addData('start_mouse.rightButton', start_mouse.rightButton)
        trials_3.addData('start_mouse.time', start_mouse.time)
        trials_3.addData('start_mouse.clicked_name', start_mouse.clicked_name)
        # the Routine "start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "trial3" ---
        # create an object to store info about Routine trial3
        trial3 = data.Routine(
            name='trial3',
            components=[target3, trial_mouse3],
        )
        trial3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        target3.setPos((random()-0.5, random()-0.5))
        # setup some python lists for storing info about the trial_mouse3
        trial_mouse3.x = []
        trial_mouse3.y = []
        trial_mouse3.leftButton = []
        trial_mouse3.midButton = []
        trial_mouse3.rightButton = []
        trial_mouse3.time = []
        trial_mouse3.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code3
        import random as rnd
        
        false_images = []
        
        trial_mouse.clickReset()
        trial_mouse.setPos((0, 0))
        
        mouseReleased = False
        
        for i in range(150):
            pos = (rnd.uniform(-0.5, 0.5), rnd.uniform(-0.5, 0.5))
        
            stim = visual.ImageStim(
                win=win,
                image='stimuli/candycane.png',
                pos=pos,
                size=(0.1, 0.1)
            )
            false_images.append(stim)
        # store start times for trial3
        trial3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        trial3.tStart = globalClock.getTime(format='float')
        trial3.status = STARTED
        thisExp.addData('trial3.started', trial3.tStart)
        trial3.maxDuration = None
        # keep track of which components have finished
        trial3Components = trial3.components
        for thisComponent in trial3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial3" ---
        thisExp.currentRoutine = trial3
        trial3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_3, 'status') and thisTrial_3.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *target3* updates
            
            # if target3 is starting this frame...
            if target3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target3.frameNStart = frameN  # exact frame index
                target3.tStart = t  # local t and not account for scr refresh
                target3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3.started')
                # update status
                target3.status = STARTED
                target3.setAutoDraw(True)
            
            # if target3 is active this frame...
            if target3.status == STARTED:
                # update params
                pass
            # *trial_mouse3* updates
            
            # if trial_mouse3 is starting this frame...
            if trial_mouse3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial_mouse3.frameNStart = frameN  # exact frame index
                trial_mouse3.tStart = t  # local t and not account for scr refresh
                trial_mouse3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial_mouse3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('trial_mouse3.started', t)
                # update status
                trial_mouse3.status = STARTED
                trial_mouse3.mouseClock.reset()
                prevButtonState = trial_mouse3.getPressed()  # if button is down already this ISN'T a new click
            if trial_mouse3.status == STARTED:  # only update if started and not finished!
                buttons = trial_mouse3.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames(target3, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(trial_mouse3):
                                gotValidClick = True
                                trial_mouse3.clicked_name.append(obj.name)
                        if not gotValidClick:
                            trial_mouse3.clicked_name.append(None)
                        x, y = trial_mouse3.getPos()
                        trial_mouse3.x.append(float(x))
                        trial_mouse3.y.append(float(y))
                        buttons = trial_mouse3.getPressed()
                        trial_mouse3.leftButton.append(buttons[0])
                        trial_mouse3.midButton.append(buttons[1])
                        trial_mouse3.rightButton.append(buttons[2])
                        trial_mouse3.time.append(trial_mouse3.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            # Run 'Each Frame' code from code3
            for stim in false_images:
                stim.draw()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=trial3,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                trial3.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if trial3.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in trial3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial3" ---
        for thisComponent in trial3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for trial3
        trial3.tStop = globalClock.getTime(format='float')
        trial3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('trial3.stopped', trial3.tStop)
        # store data for trials_3 (TrialHandler)
        trials_3.addData('trial_mouse3.x', trial_mouse3.x)
        trials_3.addData('trial_mouse3.y', trial_mouse3.y)
        trials_3.addData('trial_mouse3.leftButton', trial_mouse3.leftButton)
        trials_3.addData('trial_mouse3.midButton', trial_mouse3.midButton)
        trials_3.addData('trial_mouse3.rightButton', trial_mouse3.rightButton)
        trials_3.addData('trial_mouse3.time', trial_mouse3.time)
        trials_3.addData('trial_mouse3.clicked_name', trial_mouse3.clicked_name)
        # the Routine "trial3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "correctsound" ---
        # create an object to store info about Routine correctsound
        correctsound = data.Routine(
            name='correctsound',
            components=[correctSound],
        )
        correctsound.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        correctSound.setSound('stimuli/correct.wav', secs=2.0, hamming=True)
        correctSound.setVolume(1.0, log=False)
        correctSound.seek(0)
        # store start times for correctsound
        correctsound.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        correctsound.tStart = globalClock.getTime(format='float')
        correctsound.status = STARTED
        thisExp.addData('correctsound.started', correctsound.tStart)
        correctsound.maxDuration = None
        # keep track of which components have finished
        correctsoundComponents = correctsound.components
        for thisComponent in correctsound.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "correctsound" ---
        thisExp.currentRoutine = correctsound
        correctsound.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # if trial has changed, end Routine now
            if hasattr(thisTrial_3, 'status') and thisTrial_3.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *correctSound* updates
            
            # if correctSound is starting this frame...
            if correctSound.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                correctSound.frameNStart = frameN  # exact frame index
                correctSound.tStart = t  # local t and not account for scr refresh
                correctSound.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('correctSound.started', tThisFlipGlobal)
                # update status
                correctSound.status = STARTED
                correctSound.play(when=win)  # sync with win flip
            
            # if correctSound is stopping this frame...
            if correctSound.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > correctSound.tStartRefresh + 2.0-frameTolerance or correctSound.isFinished:
                    # keep track of stop time/frame for later
                    correctSound.tStop = t  # not accounting for scr refresh
                    correctSound.tStopRefresh = tThisFlipGlobal  # on global time
                    correctSound.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'correctSound.stopped')
                    # update status
                    correctSound.status = FINISHED
                    correctSound.stop()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=correctsound,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                correctsound.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if correctsound.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in correctsound.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "correctsound" ---
        for thisComponent in correctsound.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for correctsound
        correctsound.tStop = globalClock.getTime(format='float')
        correctsound.tStopRefresh = tThisFlipGlobal
        thisExp.addData('correctsound.stopped', correctsound.tStop)
        correctSound.pause()  # ensure sound has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if correctsound.maxDurationReached:
            routineTimer.addTime(-correctsound.maxDuration)
        elif correctsound.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        # mark thisTrial_3 as finished
        if hasattr(thisTrial_3, 'status'):
            thisTrial_3.status = FINISHED
        # if awaiting a pause, pause now
        if trials_3.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_3.status = STARTED
        thisExp.nextEntry()
        
    # completed 10 repeats of 'trials_3'
    trials_3.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "resultsscreen" ---
    # create an object to store info about Routine resultsscreen
    resultsscreen = data.Routine(
        name='resultsscreen',
        components=[thanks],
    )
    resultsscreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    thanks.reset()
    # store start times for resultsscreen
    resultsscreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    resultsscreen.tStart = globalClock.getTime(format='float')
    resultsscreen.status = STARTED
    thisExp.addData('resultsscreen.started', resultsscreen.tStart)
    resultsscreen.maxDuration = None
    # keep track of which components have finished
    resultsscreenComponents = resultsscreen.components
    for thisComponent in resultsscreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "resultsscreen" ---
    thisExp.currentRoutine = resultsscreen
    resultsscreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *thanks* updates
        
        # if thanks is starting this frame...
        if thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            thanks.frameNStart = frameN  # exact frame index
            thanks.tStart = t  # local t and not account for scr refresh
            thanks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(thanks, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thanks.started')
            # update status
            thanks.status = STARTED
            thanks.setAutoDraw(True)
        
        # if thanks is active this frame...
        if thanks.status == STARTED:
            # update params
            pass
        
        # if thanks is stopping this frame...
        if thanks.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > thanks.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                thanks.tStop = t  # not accounting for scr refresh
                thanks.tStopRefresh = tThisFlipGlobal  # on global time
                thanks.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'thanks.stopped')
                # update status
                thanks.status = FINISHED
                thanks.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=resultsscreen,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            resultsscreen.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if resultsscreen.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in resultsscreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "resultsscreen" ---
    for thisComponent in resultsscreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for resultsscreen
    resultsscreen.tStop = globalClock.getTime(format='float')
    resultsscreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('resultsscreen.stopped', resultsscreen.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if resultsscreen.maxDurationReached:
        routineTimer.addTime(-resultsscreen.maxDuration)
    elif resultsscreen.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
