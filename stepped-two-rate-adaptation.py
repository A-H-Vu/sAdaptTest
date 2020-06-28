#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on June 27, 2020, at 17:03
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'stepped-two-rate-adaptation'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '0', 'taskVer': '0'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Clifton\\Documents\\psych-proj\\stepped-two-rate-adaptation\\stepped-two-rate-adaptation.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1080, 1920], fullscr=True, screen=-1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction1"
instruction1Clock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text='Use Mouse. Space continue',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr1Resp = keyboard.Keyboard()
# Do error checking for correct values of taskVer
try:
    taskVer = int(expInfo['taskVer']) # Check to see if this is safe
except ValueError:
    taskVer = 0

# Variables to keep track of the order, rotation and target choices
orderChoice = taskVer % 6
rotationChoice = np.floor( taskVer / 12 ) % 2
targetChoice = np.floor( taskVer / 6) % 2

# Order 
order = [0,1] # Default choice
if (orderChoice == 0):
    order = [0,1]
elif (orderChoice == 1):
    order = [0,2]
elif (orderChoice == 2):
    order = [1,0]
elif (orderChoice == 3):
    order = [1,2]
elif (orderChoice == 4):
    order = [2,0]
elif (orderChoice == 5):
    order = [2,1]


# Rotation of the mouse angle
rotation = [1,-1] # Default choice
if (rotationChoice == 0):
    rotation = [1,-1]
elif (rotationChoice == 1):
    rotation = [-1,1]

# Choose set of angles for Main and Inverted task, respectively
targetAngles = [[40,50],[130,140]] # Default choice
if (targetChoice == 0):
    targetAngles = [[40,50],[130,140]]
elif (targetChoice == 1):
    targetAngles = [[130,140],[40,50]]


# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
trial1Mouse = event.Mouse(win=win)
x, y = [None, None]
trial1Mouse.mouseClock = core.Clock()
trial1Target = visual.Polygon(
    win=win, name='trial1Target',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
trial1Home = visual.Polygon(
    win=win, name='trial1Home',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
trial1Cursor = visual.Polygon(
    win=win, name='trial1Cursor',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
# Set experiment start values for variable component trial1Step
trial1Step = 0
trial1StepContainer = []
trial1Num = visual.TextStim(win=win, name='trial1Num',
    text='28',
    font='Arial',
    pos=(-0.4, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
trial1Skip = keyboard.Keyboard()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
trial2Mouse = event.Mouse(win=win)
x, y = [None, None]
trial2Mouse.mouseClock = core.Clock()
ang = None
rtd = None

#Set up rotations and main tasks
# NOTE: JS isn't automatically converted with global keyword
def setAbruptMainTask():
    print('Abrupt Main Task')
    global ang
    global rtd
    ang = rotation[0] * 30
    rtd = ang*(pi/180)

def setRampedMainTask():
    print('Ramped Main Task')
    global ang
    global rtd
    if (trials2.thisN <= 47):
        ang = rotation[0] * (trials2.thisN+1)*0.625
    else:
        ang = rotation[0] * 30
    rtd = ang*(pi/180)

def setStepMainTask():
    print('Step Main Task')
    global ang
    global rtd
    if (trials2.thisN <= 23):
        ang = rotation[0] * 7.5
    elif (trials2.thisN > 23 and trials2.thisN <= 47):
        ang = rotation[0] * 15
    elif (trials2.thisN > 47 and trials2.thisN <= 71):
        ang = rotation[0] * 22.5
    else:
        ang = rotation[0] * 30
    rtd = ang*(pi/180)

trial2Target = visual.Polygon(
    win=win, name='trial2Target',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
trial2Home = visual.Polygon(
    win=win, name='trial2Home',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
trial2Cursor = visual.Polygon(
    win=win, name='trial2Cursor',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
# Set experiment start values for variable component trial2Step
trial2Step = 0
trial2StepContainer = []
trial2Num = visual.TextStim(win=win, name='trial2Num',
    text='96',
    font='Arial',
    pos=(-0.4, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
trial2Skip = keyboard.Keyboard()
trial2Text = visual.TextStim(win=win, name='trial2Text',
    text='ang',
    font='Arial',
    pos=(-0.4, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial3"
trial3Clock = core.Clock()
trial3Mouse = event.Mouse(win=win)
x, y = [None, None]
trial3Mouse.mouseClock = core.Clock()
ang = None
rtd = None

#Set up inverses
# Might be possible combine these with the Main task functions
def setAbruptInverseTask():
    print('Abrupt Inverse Task')
    global ang
    global rtd
    ang = rotation[1] * 30
    rtd = ang*(pi/180)

def setRampedInverseTask():
    print('Ramped Inverse Task')
    global ang
    global rtd
    if (trials2.thisN <= 47):
        ang = rotation[1] * (trials2.thisN+1)*0.625
    else:
        ang = rotation[1] * 30
    rtd = ang*(pi/180)

def setStepInverseTask():
    print('Step Inverse Task')
    global ang
    global rtd
    if (trials2.thisN <= 23):
        ang = rotation[1] * 7.5
    elif (trials2.thisN > 23 and trials2.thisN <= 47):
        ang = rotation[1] * 15
    elif (trials2.thisN > 47 and trials2.thisN <= 71):
        ang = rotation[1] * 22.5
    else:
        ang = rotation[1] * 30
    rtd = ang*(pi/180)

trial3Target = visual.Polygon(
    win=win, name='trial3Target',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
trial3Home = visual.Polygon(
    win=win, name='trial3Home',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
trial3Cursor = visual.Polygon(
    win=win, name='trial3Cursor',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
# Set experiment start values for variable component trial3Step
trial3Step = 0
trial3StepContainer = []
trial3Num = visual.TextStim(win=win, name='trial3Num',
    text='8',
    font='Arial',
    pos=(-0.4, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
trial3Skip = keyboard.Keyboard()
trial3Text = visual.TextStim(win=win, name='trial3Text',
    text=None,
    font='Arial',
    pos=(-0.4, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "trial4"
trial4Clock = core.Clock()
trial4Mouse = event.Mouse(win=win)
x, y = [None, None]
trial4Mouse.mouseClock = core.Clock()
trial4Target = visual.Polygon(
    win=win, name='trial4Target',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
trial4Home = visual.Polygon(
    win=win, name='trial4Home',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
trial4Cursor = visual.Polygon(
    win=win, name='trial4Cursor',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-4.0, interpolate=True)
# Set experiment start values for variable component trial4Step
trial4Step = 0
trial4StepContainer = []
trial4Num = visual.TextStim(win=win, name='trial4Num',
    text='24',
    font='Arial',
    pos=(-0.4, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
trial4Skip = keyboard.Keyboard()
trial4Buff = visual.Polygon(
    win=win, name='trial4Buff',
    edges=180, size=[1.0, 1.0],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-8.0, interpolate=True)

# Initialize components for Routine "end"
endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='Space end',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endResp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
selectionLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('selectionVariables.xlsx'),
    seed=None, name='selectionLoop')
thisExp.addLoop(selectionLoop)  # add the loop to the experiment
thisSelectionLoop = selectionLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSelectionLoop.rgb)
if thisSelectionLoop != None:
    for paramName in thisSelectionLoop:
        exec('{} = thisSelectionLoop[paramName]'.format(paramName))

for thisSelectionLoop in selectionLoop:
    currentLoop = selectionLoop
    # abbreviate parameter names if possible (e.g. rgb = thisSelectionLoop.rgb)
    if thisSelectionLoop != None:
        for paramName in thisSelectionLoop:
            exec('{} = thisSelectionLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instruction1"-------
    continueRoutine = True
    # update component parameters for each repeat
    instr1Resp.keys = []
    instr1Resp.rt = []
    _instr1Resp_allKeys = []
    loopCount = int(loopCount) # convert the loopCount in selectionLoop to an int
    # keep track of which components have finished
    instruction1Components = [instr1, instr1Resp]
    for thisComponent in instruction1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instruction1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruction1"-------
    while continueRoutine:
        # get current time
        t = instruction1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instruction1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr1* updates
        if instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr1.frameNStart = frameN  # exact frame index
            instr1.tStart = t  # local t and not account for scr refresh
            instr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr1, 'tStartRefresh')  # time at next scr refresh
            instr1.setAutoDraw(True)
        
        # *instr1Resp* updates
        waitOnFlip = False
        if instr1Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr1Resp.frameNStart = frameN  # exact frame index
            instr1Resp.tStart = t  # local t and not account for scr refresh
            instr1Resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr1Resp, 'tStartRefresh')  # time at next scr refresh
            instr1Resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr1Resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr1Resp.status == STARTED and not waitOnFlip:
            theseKeys = instr1Resp.getKeys(keyList=['space'], waitRelease=False)
            _instr1Resp_allKeys.extend(theseKeys)
            if len(_instr1Resp_allKeys):
                instr1Resp.keys = _instr1Resp_allKeys[-1].name  # just the last key pressed
                instr1Resp.rt = _instr1Resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruction1"-------
    for thisComponent in instruction1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    selectionLoop.addData('instr1.started', instr1.tStartRefresh)
    selectionLoop.addData('instr1.stopped', instr1.tStopRefresh)
    # the Routine "instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fix]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    selectionLoop.addData('fix.started', fix.tStartRefresh)
    selectionLoop.addData('fix.stopped', fix.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials1 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials1Cond.xlsx'),
        seed=None, name='trials1')
    thisExp.addLoop(trials1)  # add the loop to the experiment
    thisTrials1 = trials1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
    if thisTrials1 != None:
        for paramName in thisTrials1:
            exec('{} = thisTrials1[paramName]'.format(paramName))
    
    for thisTrials1 in trials1:
        currentLoop = trials1
        # abbreviate parameter names if possible (e.g. rgb = thisTrials1.rgb)
        if thisTrials1 != None:
            for paramName in thisTrials1:
                exec('{} = thisTrials1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial1"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the trial1Mouse
        trial1Mouse.x = []
        trial1Mouse.y = []
        trial1Mouse.leftButton = []
        trial1Mouse.midButton = []
        trial1Mouse.rightButton = []
        trial1Mouse.time = []
        gotValidClick = False  # until a click is received
        trial1Mouse.mouseClock.reset()
        win.mouseVisible = False
        
        targetangle = targetAngles[loopCount][trials1.thisN % 2] # targetAngles defined in instruction1
        targetangle_rad = pi*(targetangle/180)
        targetPos = (cos(targetangle_rad)*0.4, sin(targetangle_rad)*0.4)
        
        targetOpacity = 0
        homeOpacity = 0
        
        homeStart = False
        reachOut = False
        
        trial1Step = 1
        steps = []
        
        print("Align task")
        #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
        trial1Num.text = str(trials1.thisN+1)+' / 36'
        
        trial1Cursor.pos = (1.5,1.5)
        trial1Mouse.pos = (1.5,1.5)
        trial1Skip.keys = []
        trial1Skip.rt = []
        _trial1Skip_allKeys = []
        # keep track of which components have finished
        trial1Components = [trial1Mouse, trial1Target, trial1Home, trial1Cursor, trial1Num, trial1Skip]
        for thisComponent in trial1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial1"-------
        while continueRoutine:
            # get current time
            t = trial1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *trial1Mouse* updates
            if trial1Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial1Mouse.frameNStart = frameN  # exact frame index
                trial1Mouse.tStart = t  # local t and not account for scr refresh
                trial1Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial1Mouse, 'tStartRefresh')  # time at next scr refresh
                trial1Mouse.status = STARTED
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if trial1Mouse.status == STARTED:  # only update if started and not finished!
                x, y = trial1Mouse.getPos()
                trial1Mouse.x.append(x)
                trial1Mouse.y.append(y)
                buttons = trial1Mouse.getPressed()
                trial1Mouse.leftButton.append(buttons[0])
                trial1Mouse.midButton.append(buttons[1])
                trial1Mouse.rightButton.append(buttons[2])
                trial1Mouse.time.append(trial1Mouse.mouseClock.getTime())
            CursorTargetDistance = sqrt((trial1Cursor.pos[0]-trial1Target.pos[0])**2 + (trial1Cursor.pos[1]-trial1Target.pos[1])**2)
            CursorHomeDistance = sqrt(trial1Cursor.pos[0]**2 + trial1Cursor.pos[1]**2)
            
            steps.append(trial1Step)
            # steps.push(step)
            
            if not(homeStart):
                homeOpacity = 1
                targetOpacity = 0
                trial1Step = 1
                if (CursorHomeDistance < .025):
                    homeStart = True
                    print('end step 1'+' ('+str(globalClock.getTime())+')')
            
            if (not(reachOut) and homeStart):
                homeOpacity = 0
                targetOpacity = 1
                trial1Step = 2
                if (CursorTargetDistance < .025):
                    reachOut = True
                    print('end step 2'+' ('+str(globalClock.getTime())+')')
            
            if (reachOut):
                homeOpacity = 1
                targetOpacity = 0
                trial1Step = 3
                if (CursorHomeDistance < .025):
                    # maybe this ends the loop prematurely?
                    print('end step 3'+' ('+str(globalClock.getTime())+')')
                    continueRoutine = False
                    
            #steps = steps.append(step)
            
            # *trial1Target* updates
            if trial1Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial1Target.frameNStart = frameN  # exact frame index
                trial1Target.tStart = t  # local t and not account for scr refresh
                trial1Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial1Target, 'tStartRefresh')  # time at next scr refresh
                trial1Target.setAutoDraw(True)
            if trial1Target.status == STARTED:  # only update if drawing
                trial1Target.setOpacity(targetOpacity, log=False)
                trial1Target.setPos(targetPos, log=False)
            
            # *trial1Home* updates
            if trial1Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial1Home.frameNStart = frameN  # exact frame index
                trial1Home.tStart = t  # local t and not account for scr refresh
                trial1Home.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial1Home, 'tStartRefresh')  # time at next scr refresh
                trial1Home.setAutoDraw(True)
            if trial1Home.status == STARTED:  # only update if drawing
                trial1Home.setOpacity(homeOpacity, log=False)
            
            # *trial1Cursor* updates
            if trial1Cursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial1Cursor.frameNStart = frameN  # exact frame index
                trial1Cursor.tStart = t  # local t and not account for scr refresh
                trial1Cursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial1Cursor, 'tStartRefresh')  # time at next scr refresh
                trial1Cursor.setAutoDraw(True)
            if trial1Cursor.status == STARTED:  # only update if drawing
                trial1Cursor.setPos((trial1Mouse.getPos()[0], trial1Mouse.getPos()[1]), log=False)
            
            # *trial1Num* updates
            if trial1Num.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial1Num.frameNStart = frameN  # exact frame index
                trial1Num.tStart = t  # local t and not account for scr refresh
                trial1Num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial1Num, 'tStartRefresh')  # time at next scr refresh
                trial1Num.setAutoDraw(True)
            
            # *trial1Skip* updates
            waitOnFlip = False
            if trial1Skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial1Skip.frameNStart = frameN  # exact frame index
                trial1Skip.tStart = t  # local t and not account for scr refresh
                trial1Skip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial1Skip, 'tStartRefresh')  # time at next scr refresh
                trial1Skip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trial1Skip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trial1Skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trial1Skip.status == STARTED and not waitOnFlip:
                theseKeys = trial1Skip.getKeys(keyList=['space'], waitRelease=False)
                _trial1Skip_allKeys.extend(theseKeys)
                if len(_trial1Skip_allKeys):
                    trial1Skip.keys = _trial1Skip_allKeys[-1].name  # just the last key pressed
                    trial1Skip.rt = _trial1Skip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial1"-------
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials1 (TrialHandler)
        trials1.addData('trial1Mouse.x', trial1Mouse.x)
        trials1.addData('trial1Mouse.y', trial1Mouse.y)
        trials1.addData('trial1Mouse.leftButton', trial1Mouse.leftButton)
        trials1.addData('trial1Mouse.midButton', trial1Mouse.midButton)
        trials1.addData('trial1Mouse.rightButton', trial1Mouse.rightButton)
        trials1.addData('trial1Mouse.time', trial1Mouse.time)
        trials1.addData('trial1Mouse.started', trial1Mouse.tStartRefresh)
        trials1.addData('trial1Mouse.stopped', trial1Mouse.tStopRefresh)
        # thisExp.addData('step', stepvector)
        thisExp.addData('step', steps)
        thisExp.addData('targetangle_deg', targetangle)
        
        # psychoJS.experiment.addData('columnName', variable)
        #psychoJS.experiment.addData('step', steps)
        #psychoJS.experiment.addData('targetangle_deg', targetangle)
        trials1.addData('trial1Target.started', trial1Target.tStartRefresh)
        trials1.addData('trial1Target.stopped', trial1Target.tStopRefresh)
        trials1.addData('trial1Home.started', trial1Home.tStartRefresh)
        trials1.addData('trial1Home.stopped', trial1Home.tStopRefresh)
        trials1.addData('trial1Cursor.started', trial1Cursor.tStartRefresh)
        trials1.addData('trial1Cursor.stopped', trial1Cursor.tStopRefresh)
        trials1.addData('trial1Num.started', trial1Num.tStartRefresh)
        trials1.addData('trial1Num.stopped', trial1Num.tStopRefresh)
        # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials1'
    
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fix]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    selectionLoop.addData('fix.started', fix.tStartRefresh)
    selectionLoop.addData('fix.stopped', fix.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials2 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials2Cond.xlsx'),
        seed=None, name='trials2')
    thisExp.addLoop(trials2)  # add the loop to the experiment
    thisTrials2 = trials2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
    if thisTrials2 != None:
        for paramName in thisTrials2:
            exec('{} = thisTrials2[paramName]'.format(paramName))
    
    for thisTrials2 in trials2:
        currentLoop = trials2
        # abbreviate parameter names if possible (e.g. rgb = thisTrials2.rgb)
        if thisTrials2 != None:
            for paramName in thisTrials2:
                exec('{} = thisTrials2[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial2"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the trial2Mouse
        trial2Mouse.x = []
        trial2Mouse.y = []
        trial2Mouse.leftButton = []
        trial2Mouse.midButton = []
        trial2Mouse.rightButton = []
        trial2Mouse.time = []
        gotValidClick = False  # until a click is received
        trial2Mouse.mouseClock.reset()
        targetangle = targetAngles[0][trials2.thisN % 2]
        targetangle_rad = pi*(targetangle/180)
        targetPos = (cos(targetangle_rad)*0.4, sin(targetangle_rad)*0.4)
        
        targetOpacity = 0
        homeOpacity = 0
        
        homeStart = False
        reachOut = False
        
        trial2Step = 1
        steps = []
        
        #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
        trial2Num.text = str(trials2.thisN+1)+' / 96'
        
        trial2Cursor.pos = (1.5,1.5)
        trial2Mouse.pos = (1.5,1.5)
        
        task = order[loopCount] # loopCount taken from the selectionVariables.xlsx
        
        if (task == 0):
            setAbruptMainTask()
        elif (task == 1):
            setRampedMainTask()
        elif (task == 2):
            setStepMainTask()
        else:
            setAbruptMainTask() # Contingency condition don't know if this is needed
        
        trial2Text.text = str(ang)
        trial2Skip.keys = []
        trial2Skip.rt = []
        _trial2Skip_allKeys = []
        # keep track of which components have finished
        trial2Components = [trial2Mouse, trial2Target, trial2Home, trial2Cursor, trial2Num, trial2Skip, trial2Text]
        for thisComponent in trial2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial2"-------
        while continueRoutine:
            # get current time
            t = trial2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *trial2Mouse* updates
            if trial2Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial2Mouse.frameNStart = frameN  # exact frame index
                trial2Mouse.tStart = t  # local t and not account for scr refresh
                trial2Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial2Mouse, 'tStartRefresh')  # time at next scr refresh
                trial2Mouse.status = STARTED
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if trial2Mouse.status == STARTED:  # only update if started and not finished!
                x, y = trial2Mouse.getPos()
                trial2Mouse.x.append(x)
                trial2Mouse.y.append(y)
                buttons = trial2Mouse.getPressed()
                trial2Mouse.leftButton.append(buttons[0])
                trial2Mouse.midButton.append(buttons[1])
                trial2Mouse.rightButton.append(buttons[2])
                trial2Mouse.time.append(trial2Mouse.mouseClock.getTime())
            CursorTargetDistance = sqrt((trial2Cursor.pos[0]-trial2Target.pos[0])**2 + (trial2Cursor.pos[1]-trial2Target.pos[1])**2)
            CursorHomeDistance = sqrt(trial2Cursor.pos[0]**2 + trial2Cursor.pos[1]**2)
            
            steps.append(trial2Step)
            # steps.push(step)
            
            if not(homeStart):
                homeOpacity = 1
                targetOpacity = 0
                trial2Step = 1
                if (CursorHomeDistance < .025):
                    homeStart = True
                    print('end step 1'+' ('+str(globalClock.getTime())+')')
            
            if (not(reachOut) and homeStart):
                homeOpacity = 0
                targetOpacity = 1
                trial2Step = 2
                if (CursorTargetDistance < .025):
                    reachOut = True
                    print('end step 2'+' ('+str(globalClock.getTime())+')')
            
            if (reachOut):
                homeOpacity = 1
                targetOpacity = 0
                trial2Step = 3
                if (CursorHomeDistance < .025):
                    # maybe this ends the loop prematurely?
                    print('end step 3'+' ('+str(globalClock.getTime())+')')
                    continueRoutine = False
                    
            #steps = steps.append(step)
            
            # *trial2Target* updates
            if trial2Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial2Target.frameNStart = frameN  # exact frame index
                trial2Target.tStart = t  # local t and not account for scr refresh
                trial2Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial2Target, 'tStartRefresh')  # time at next scr refresh
                trial2Target.setAutoDraw(True)
            if trial2Target.status == STARTED:  # only update if drawing
                trial2Target.setOpacity(targetOpacity, log=False)
                trial2Target.setPos(targetPos, log=False)
            
            # *trial2Home* updates
            if trial2Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial2Home.frameNStart = frameN  # exact frame index
                trial2Home.tStart = t  # local t and not account for scr refresh
                trial2Home.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial2Home, 'tStartRefresh')  # time at next scr refresh
                trial2Home.setAutoDraw(True)
            if trial2Home.status == STARTED:  # only update if drawing
                trial2Home.setOpacity(homeOpacity, log=False)
            
            # *trial2Cursor* updates
            if trial2Cursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial2Cursor.frameNStart = frameN  # exact frame index
                trial2Cursor.tStart = t  # local t and not account for scr refresh
                trial2Cursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial2Cursor, 'tStartRefresh')  # time at next scr refresh
                trial2Cursor.setAutoDraw(True)
            if trial2Cursor.status == STARTED:  # only update if drawing
                trial2Cursor.setPos(((trial2Mouse.getPos()[0]*cos(rtd))-(trial2Mouse.getPos()[1]*sin(rtd)), (trial2Mouse.getPos()[0]*sin(rtd))+(trial2Mouse.getPos()[1]*cos(rtd))), log=False)
            
            # *trial2Num* updates
            if trial2Num.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial2Num.frameNStart = frameN  # exact frame index
                trial2Num.tStart = t  # local t and not account for scr refresh
                trial2Num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial2Num, 'tStartRefresh')  # time at next scr refresh
                trial2Num.setAutoDraw(True)
            
            # *trial2Skip* updates
            waitOnFlip = False
            if trial2Skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial2Skip.frameNStart = frameN  # exact frame index
                trial2Skip.tStart = t  # local t and not account for scr refresh
                trial2Skip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial2Skip, 'tStartRefresh')  # time at next scr refresh
                trial2Skip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trial2Skip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trial2Skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trial2Skip.status == STARTED and not waitOnFlip:
                theseKeys = trial2Skip.getKeys(keyList=['space'], waitRelease=False)
                _trial2Skip_allKeys.extend(theseKeys)
                if len(_trial2Skip_allKeys):
                    trial2Skip.keys = _trial2Skip_allKeys[-1].name  # just the last key pressed
                    trial2Skip.rt = _trial2Skip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *trial2Text* updates
            if trial2Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial2Text.frameNStart = frameN  # exact frame index
                trial2Text.tStart = t  # local t and not account for scr refresh
                trial2Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial2Text, 'tStartRefresh')  # time at next scr refresh
                trial2Text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial2"-------
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials2 (TrialHandler)
        trials2.addData('trial2Mouse.x', trial2Mouse.x)
        trials2.addData('trial2Mouse.y', trial2Mouse.y)
        trials2.addData('trial2Mouse.leftButton', trial2Mouse.leftButton)
        trials2.addData('trial2Mouse.midButton', trial2Mouse.midButton)
        trials2.addData('trial2Mouse.rightButton', trial2Mouse.rightButton)
        trials2.addData('trial2Mouse.time', trial2Mouse.time)
        trials2.addData('trial2Mouse.started', trial2Mouse.tStartRefresh)
        trials2.addData('trial2Mouse.stopped', trial2Mouse.tStopRefresh)
        # thisExp.addData('step', stepvector)
        thisExp.addData('step', steps)
        thisExp.addData('targetangle_deg', targetangle)
        
        # psychoJS.experiment.addData('columnName', variable)
        #psychoJS.experiment.addData('step', steps)
        #psychoJS.experiment.addData('targetangle_deg', targetangle)
        trials2.addData('trial2Target.started', trial2Target.tStartRefresh)
        trials2.addData('trial2Target.stopped', trial2Target.tStopRefresh)
        trials2.addData('trial2Home.started', trial2Home.tStartRefresh)
        trials2.addData('trial2Home.stopped', trial2Home.tStopRefresh)
        trials2.addData('trial2Cursor.started', trial2Cursor.tStartRefresh)
        trials2.addData('trial2Cursor.stopped', trial2Cursor.tStopRefresh)
        trials2.addData('trial2Num.started', trial2Num.tStartRefresh)
        trials2.addData('trial2Num.stopped', trial2Num.tStopRefresh)
        trials2.addData('trial2Text.started', trial2Text.tStartRefresh)
        trials2.addData('trial2Text.stopped', trial2Text.tStopRefresh)
        # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials2'
    
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fix]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    selectionLoop.addData('fix.started', fix.tStartRefresh)
    selectionLoop.addData('fix.stopped', fix.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials3Cond.xlsx'),
        seed=None, name='trials3')
    thisExp.addLoop(trials3)  # add the loop to the experiment
    thisTrials3 = trials3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
    if thisTrials3 != None:
        for paramName in thisTrials3:
            exec('{} = thisTrials3[paramName]'.format(paramName))
    
    for thisTrials3 in trials3:
        currentLoop = trials3
        # abbreviate parameter names if possible (e.g. rgb = thisTrials3.rgb)
        if thisTrials3 != None:
            for paramName in thisTrials3:
                exec('{} = thisTrials3[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial3"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the trial3Mouse
        trial3Mouse.x = []
        trial3Mouse.y = []
        trial3Mouse.leftButton = []
        trial3Mouse.midButton = []
        trial3Mouse.rightButton = []
        trial3Mouse.time = []
        gotValidClick = False  # until a click is received
        trial3Mouse.mouseClock.reset()
        win.mouseVisible = False
        
        targetangle = targetAngles[loopCount][trials3.thisN % 2] # Alternate between the 2 choices
        targetangle_rad = pi*(targetangle/180)
        targetPos = (cos(targetangle_rad)*0.4, sin(targetangle_rad)*0.4)
        
        targetOpacity = 0
        homeOpacity = 0
        
        homeStart = False
        reachOut = False
        
        trial3Step = 1
        steps = []
        
        #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
        trial3Num.text = str(trials3.thisN+1)+' / 8'
        
        trial3Cursor.pos = (1.5,1.5)
        trial3Mouse.pos = (1.5,1.5)
        
        task = order[loopCount]
        
        if (task == 0):
            setAbruptInverseTask()
        elif (task == 1):
            setRampedInverseTask()
        elif (task == 2):
            setStepInverseTask()
        else:
            setAbruptInverseTask() # Contingency condition don't know if this is needed
                
        trial3Text.text = str(ang)
        trial3Skip.keys = []
        trial3Skip.rt = []
        _trial3Skip_allKeys = []
        # keep track of which components have finished
        trial3Components = [trial3Mouse, trial3Target, trial3Home, trial3Cursor, trial3Num, trial3Skip, trial3Text]
        for thisComponent in trial3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial3"-------
        while continueRoutine:
            # get current time
            t = trial3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *trial3Mouse* updates
            if trial3Mouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial3Mouse.frameNStart = frameN  # exact frame index
                trial3Mouse.tStart = t  # local t and not account for scr refresh
                trial3Mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial3Mouse, 'tStartRefresh')  # time at next scr refresh
                trial3Mouse.status = STARTED
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if trial3Mouse.status == STARTED:  # only update if started and not finished!
                x, y = trial3Mouse.getPos()
                trial3Mouse.x.append(x)
                trial3Mouse.y.append(y)
                buttons = trial3Mouse.getPressed()
                trial3Mouse.leftButton.append(buttons[0])
                trial3Mouse.midButton.append(buttons[1])
                trial3Mouse.rightButton.append(buttons[2])
                trial3Mouse.time.append(trial3Mouse.mouseClock.getTime())
            CursorTargetDistance = sqrt((trial3Cursor.pos[0]-trial3Target.pos[0])**2 + (trial3Cursor.pos[1]-trial3Target.pos[1])**2)
            CursorHomeDistance = sqrt(trial3Cursor.pos[0]**2 + trial3Cursor.pos[1]**2)
            
            steps.append(trial3Step)
            # steps.push(step)
            
            if not(homeStart):
                homeOpacity = 1
                targetOpacity = 0
                trial3Step = 1
                if (CursorHomeDistance < .025):
                    homeStart = True
                    print('end step 1'+' ('+str(globalClock.getTime())+')')
            
            if (not(reachOut) and homeStart):
                homeOpacity = 0
                targetOpacity = 1
                trial3Step = 2
                if (CursorTargetDistance < .025):
                    reachOut = True
                    print('end step 2'+' ('+str(globalClock.getTime())+')')
            
            if (reachOut):
                homeOpacity = 1
                targetOpacity = 0
                trial3Step = 3
                if (CursorHomeDistance < .025):
                    # maybe this ends the loop prematurely?
                    print('end step 3'+' ('+str(globalClock.getTime())+')')
                    continueRoutine = False
                    
            #steps = steps.append(step)
            
            # *trial3Target* updates
            if trial3Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial3Target.frameNStart = frameN  # exact frame index
                trial3Target.tStart = t  # local t and not account for scr refresh
                trial3Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial3Target, 'tStartRefresh')  # time at next scr refresh
                trial3Target.setAutoDraw(True)
            if trial3Target.status == STARTED:  # only update if drawing
                trial3Target.setOpacity(targetOpacity, log=False)
                trial3Target.setPos(targetPos, log=False)
            
            # *trial3Home* updates
            if trial3Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial3Home.frameNStart = frameN  # exact frame index
                trial3Home.tStart = t  # local t and not account for scr refresh
                trial3Home.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial3Home, 'tStartRefresh')  # time at next scr refresh
                trial3Home.setAutoDraw(True)
            if trial3Home.status == STARTED:  # only update if drawing
                trial3Home.setOpacity(homeOpacity, log=False)
            
            # *trial3Cursor* updates
            if trial3Cursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial3Cursor.frameNStart = frameN  # exact frame index
                trial3Cursor.tStart = t  # local t and not account for scr refresh
                trial3Cursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial3Cursor, 'tStartRefresh')  # time at next scr refresh
                trial3Cursor.setAutoDraw(True)
            if trial3Cursor.status == STARTED:  # only update if drawing
                trial3Cursor.setPos(((trial3Mouse.getPos()[0]*cos(rtd))-(trial3Mouse.getPos()[1]*sin(rtd)), (trial3Mouse.getPos()[0]*sin(rtd))+(trial3Mouse.getPos()[1]*cos(rtd))), log=False)
            
            # *trial3Num* updates
            if trial3Num.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial3Num.frameNStart = frameN  # exact frame index
                trial3Num.tStart = t  # local t and not account for scr refresh
                trial3Num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial3Num, 'tStartRefresh')  # time at next scr refresh
                trial3Num.setAutoDraw(True)
            
            # *trial3Skip* updates
            waitOnFlip = False
            if trial3Skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial3Skip.frameNStart = frameN  # exact frame index
                trial3Skip.tStart = t  # local t and not account for scr refresh
                trial3Skip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial3Skip, 'tStartRefresh')  # time at next scr refresh
                trial3Skip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trial3Skip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trial3Skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trial3Skip.status == STARTED and not waitOnFlip:
                theseKeys = trial3Skip.getKeys(keyList=['space'], waitRelease=False)
                _trial3Skip_allKeys.extend(theseKeys)
                if len(_trial3Skip_allKeys):
                    trial3Skip.keys = _trial3Skip_allKeys[-1].name  # just the last key pressed
                    trial3Skip.rt = _trial3Skip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *trial3Text* updates
            if trial3Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial3Text.frameNStart = frameN  # exact frame index
                trial3Text.tStart = t  # local t and not account for scr refresh
                trial3Text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial3Text, 'tStartRefresh')  # time at next scr refresh
                trial3Text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial3"-------
        for thisComponent in trial3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials3 (TrialHandler)
        trials3.addData('trial3Mouse.x', trial3Mouse.x)
        trials3.addData('trial3Mouse.y', trial3Mouse.y)
        trials3.addData('trial3Mouse.leftButton', trial3Mouse.leftButton)
        trials3.addData('trial3Mouse.midButton', trial3Mouse.midButton)
        trials3.addData('trial3Mouse.rightButton', trial3Mouse.rightButton)
        trials3.addData('trial3Mouse.time', trial3Mouse.time)
        trials3.addData('trial3Mouse.started', trial3Mouse.tStartRefresh)
        trials3.addData('trial3Mouse.stopped', trial3Mouse.tStopRefresh)
        # thisExp.addData('step', stepvector)
        thisExp.addData('step', steps)
        thisExp.addData('targetangle_deg', targetangle)
        
        # psychoJS.experiment.addData('columnName', variable)
        #psychoJS.experiment.addData('step', steps)
        #psychoJS.experiment.addData('targetangle_deg', targetangle)
        trials3.addData('trial3Target.started', trial3Target.tStartRefresh)
        trials3.addData('trial3Target.stopped', trial3Target.tStopRefresh)
        trials3.addData('trial3Home.started', trial3Home.tStartRefresh)
        trials3.addData('trial3Home.stopped', trial3Home.tStopRefresh)
        trials3.addData('trial3Cursor.started', trial3Cursor.tStartRefresh)
        trials3.addData('trial3Cursor.stopped', trial3Cursor.tStopRefresh)
        trials3.addData('trial3Num.started', trial3Num.tStartRefresh)
        trials3.addData('trial3Num.stopped', trial3Num.tStopRefresh)
        trials3.addData('trial3Text.started', trial3Text.tStartRefresh)
        trials3.addData('trial3Text.stopped', trial3Text.tStopRefresh)
        # the Routine "trial3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials3'
    
    
    # set up handler to look after randomisation of conditions etc
    trials4 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trials4Cond.xlsx'),
        seed=None, name='trials4')
    thisExp.addLoop(trials4)  # add the loop to the experiment
    thisTrials4 = trials4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials4.rgb)
    if thisTrials4 != None:
        for paramName in thisTrials4:
            exec('{} = thisTrials4[paramName]'.format(paramName))
    
    for thisTrials4 in trials4:
        currentLoop = trials4
        # abbreviate parameter names if possible (e.g. rgb = thisTrials4.rgb)
        if thisTrials4 != None:
            for paramName in thisTrials4:
                exec('{} = thisTrials4[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial4"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the trial4Mouse
        gotValidClick = False  # until a click is received
        trial4Mouse.mouseClock.reset()
        targetangle = targetAngles[loopCount][trials4.thisN % 2]
        targetangle_rad = pi*(targetangle/180)
        targetPos = (cos(targetangle_rad)*0.4, sin(targetangle_rad)*0.4)
        
        targetOpacity = 0
        homeOpacity = 0
        #'buffer' circle set up
        bufferOpacity = 0
        bufferRadius = (sqrt(trial4Cursor.pos[0]**2 + trial4Cursor.pos[1]**2))
        #allows cursor opacity changing
        cursorOpacity = 0
        
        homeStart = False
        reachOut = False
        
        trial4Step = 1
        steps = []
        
        #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
        trial4Num.text = str(trials4.thisN+1)+' / 24'
        
        trial4Cursor.pos = (1.5,1.5)
        trial4Mouse.pos = (1.5,1.5)
        
        theta = (targetangle / 180) * pi
        
        print('Error Clamped Task')
        trial4Skip.keys = []
        trial4Skip.rt = []
        _trial4Skip_allKeys = []
        # keep track of which components have finished
        trial4Components = [trial4Mouse, trial4Target, trial4Home, trial4Cursor, trial4Num, trial4Skip, trial4Buff]
        for thisComponent in trial4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial4"-------
        while continueRoutine:
            # get current time
            t = trial4Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial4Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            CursorTargetDistance = sqrt((trial4Cursor.pos[0]-trial4Target.pos[0])**2 + (trial4Cursor.pos[1]-trial4Target.pos[1])**2)
            CursorHomeDistance = sqrt(trial4Cursor.pos[0]**2 + trial4Cursor.pos[1]**2)
            
            steps.append(trial3Step)
            # steps.push(step)
            
            if not(homeStart):
                homeOpacity = 1
                targetOpacity = 0
                trial4Step = 1
                bufferOpacity = 0
                cursorOpacity = 1
                if (CursorHomeDistance < .075):
                    homeStart = True
                    print('end step 1'+' ('+str(globalClock.getTime())+')')
            
            if (not(reachOut) and homeStart):
                homeOpacity = 0
                targetOpacity = 1
                trial4Step = 2
                bufferOpacity = 0
                cursorOpacity = 1
                if (CursorTargetDistance < .025):
                    reachOut = True
                    print('end step 2'+' ('+str(globalClock.getTime())+')')
            
            if (reachOut):
                homeOpacity = 1
                targetOpacity = 0
                trial4Step = 3
                #COntrols the 'buffer'
                bufferOpacity = 1
                bufferRadius = (sqrt(trial4Cursor.pos[0]**2 + trial4Cursor.pos[1]**2))
                #controls the cursor
                cursorOpacity = 0
                if (CursorHomeDistance < .2):
                    cursorOpacity = 1
                if (CursorHomeDistance < .075):
                    # maybe this ends the loop prematurely?
                    print('end step 3'+' ('+str(globalClock.getTime())+')')
                    continueRoutine = False
                    
            #steps = steps.append(step)
            
            # *trial4Target* updates
            if trial4Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial4Target.frameNStart = frameN  # exact frame index
                trial4Target.tStart = t  # local t and not account for scr refresh
                trial4Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial4Target, 'tStartRefresh')  # time at next scr refresh
                trial4Target.setAutoDraw(True)
            if trial4Target.status == STARTED:  # only update if drawing
                trial4Target.setOpacity(targetOpacity, log=False)
                trial4Target.setPos(targetPos, log=False)
            
            # *trial4Home* updates
            if trial4Home.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial4Home.frameNStart = frameN  # exact frame index
                trial4Home.tStart = t  # local t and not account for scr refresh
                trial4Home.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial4Home, 'tStartRefresh')  # time at next scr refresh
                trial4Home.setAutoDraw(True)
            if trial4Home.status == STARTED:  # only update if drawing
                trial4Home.setOpacity(homeOpacity, log=False)
            
            # *trial4Cursor* updates
            if trial4Cursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial4Cursor.frameNStart = frameN  # exact frame index
                trial4Cursor.tStart = t  # local t and not account for scr refresh
                trial4Cursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial4Cursor, 'tStartRefresh')  # time at next scr refresh
                trial4Cursor.setAutoDraw(True)
            if trial4Cursor.status == STARTED:  # only update if drawing
                trial4Cursor.setOpacity(cursorOpacity, log=False)
                trial4Cursor.setPos((sqrt((trial4Mouse.getPos()[0]**2)+(trial4Mouse.getPos()[1]**2))*(cos(theta)), sqrt((trial4Mouse.getPos()[0]**2)+(trial4Mouse.getPos()[1]**2))*(sin(theta))), log=False)
            
            # *trial4Num* updates
            if trial4Num.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial4Num.frameNStart = frameN  # exact frame index
                trial4Num.tStart = t  # local t and not account for scr refresh
                trial4Num.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial4Num, 'tStartRefresh')  # time at next scr refresh
                trial4Num.setAutoDraw(True)
            
            # *trial4Skip* updates
            waitOnFlip = False
            if trial4Skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial4Skip.frameNStart = frameN  # exact frame index
                trial4Skip.tStart = t  # local t and not account for scr refresh
                trial4Skip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial4Skip, 'tStartRefresh')  # time at next scr refresh
                trial4Skip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trial4Skip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trial4Skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trial4Skip.status == STARTED and not waitOnFlip:
                theseKeys = trial4Skip.getKeys(keyList=['space'], waitRelease=False)
                _trial4Skip_allKeys.extend(theseKeys)
                if len(_trial4Skip_allKeys):
                    trial4Skip.keys = _trial4Skip_allKeys[-1].name  # just the last key pressed
                    trial4Skip.rt = _trial4Skip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *trial4Buff* updates
            if trial4Buff.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trial4Buff.frameNStart = frameN  # exact frame index
                trial4Buff.tStart = t  # local t and not account for scr refresh
                trial4Buff.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trial4Buff, 'tStartRefresh')  # time at next scr refresh
                trial4Buff.setAutoDraw(True)
            if trial4Buff.status == STARTED:  # only update if drawing
                trial4Buff.setOpacity(bufferOpacity, log=False)
                trial4Buff.setSize(bufferRadius, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial4"-------
        for thisComponent in trial4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials4 (TrialHandler)
        trials4.addData('trial4Mouse.started', trial4Mouse.tStartRefresh)
        trials4.addData('trial4Mouse.stopped', trial4Mouse.tStopRefresh)
        # thisExp.addData('step', stepvector)
        thisExp.addData('step', steps)
        thisExp.addData('targetangle_deg', targetangle)
        
        # psychoJS.experiment.addData('columnName', variable)
        #psychoJS.experiment.addData('step', steps)
        #psychoJS.experiment.addData('targetangle_deg', targetangle)
        trials4.addData('trial4Target.started', trial4Target.tStartRefresh)
        trials4.addData('trial4Target.stopped', trial4Target.tStopRefresh)
        trials4.addData('trial4Home.started', trial4Home.tStartRefresh)
        trials4.addData('trial4Home.stopped', trial4Home.tStopRefresh)
        trials4.addData('trial4Cursor.started', trial4Cursor.tStartRefresh)
        trials4.addData('trial4Cursor.stopped', trial4Cursor.tStopRefresh)
        trials4.addData('trial4Num.started', trial4Num.tStartRefresh)
        trials4.addData('trial4Num.stopped', trial4Num.tStopRefresh)
        trials4.addData('trial4Buff.started', trial4Buff.tStartRefresh)
        trials4.addData('trial4Buff.stopped', trial4Buff.tStopRefresh)
        # the Routine "trial4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials4'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'selectionLoop'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
endResp.keys = []
endResp.rt = []
_endResp_allKeys = []
# keep track of which components have finished
endComponents = [endText, endResp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    
    # *endResp* updates
    waitOnFlip = False
    if endResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endResp.frameNStart = frameN  # exact frame index
        endResp.tStart = t  # local t and not account for scr refresh
        endResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endResp, 'tStartRefresh')  # time at next scr refresh
        endResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endResp.status == STARTED and not waitOnFlip:
        theseKeys = endResp.getKeys(keyList=['space'], waitRelease=False)
        _endResp_allKeys.extend(theseKeys)
        if len(_endResp_allKeys):
            endResp.keys = _endResp_allKeys[-1].name  # just the last key pressed
            endResp.rt = _endResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.mouseVisible = True

# psychoJS.window.mouseVisible = true;
win.mouseVisible = True

# psychoJS.window.mouseVisible = true;
win.mouseVisible = True

# psychoJS.window.mouseVisible = true;
win.mouseVisible = True

# psychoJS.window.mouseVisible = true;

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
