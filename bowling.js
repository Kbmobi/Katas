//Set up 10(+2) frames
var arrGame = [];
for (var i = 0; i < 12; i++) {
    arrGame.push({
        intFrame: i,
        intBall1: null,
        intBall2: null,
      	blnStrike: null,
        blnSpare: null,
		intScore: null
    });
}

//handle rolling input frame, ball 1 ore 2, and how many pins. No error checking right now
function bowl(intFrameNumber, intBallNumber, intPinsHit) {
  switch(intBallNumber) {
    case 1:
      	if(intPinsHit == 10) {
          arrGame[intFrameNumber].blnStrike = true;
        }
        arrGame[intFrameNumber].intBall1 = intPinsHit;
        break;
    case 2:
      	var temp = intPinsHit + arrGame[intFrameNumber].intBall1;
      	if(temp == 10) {
          arrGame[intFrameNumber].blnSpare = true;
        }
      	arrGame[intFrameNumber].intBall2 = intPinsHit;
        break;
		}
}
//tally up entire game score
function score(intFrameNumber) {
	for (var i = 0; i < intFrameNumber; i++) {
		var score = null;
		
		if (arrGame[i].blnStrike == true && i < 11) {
			if (arrGame[i+1].blnStrike == true && i < 10) {
				if (arrGame[i+2].blnStrike == true) {
					score = 30;
				} else {
					score = 20 + arrGame[i+2].intBall1;
				}
			} else {
				score = 10 + arrGame[i+1].intBall1 + arrGame[i+1].intBall2;
			}
		} else if (arrGame[i].blnSpare == true) {
			score = 10 + arrGame[i].intBall1;
		} else {
			score = arrGame[i].intBall1 + arrGame[i].intBall2;
		}
    
		if (i > 0) {
			score += arrGame[i-1].intScore; 
		}
		arrGame[i].intScore = score;
	}
}

function strike() {
	return 10;
}

bowl(0,1,10);
bowl(1,1,10);
bowl(2,1,10);
bowl(3,1,10);
bowl(4,1,10);
bowl(5,1,10);
bowl(6,1,10);
bowl(7,1,10);
bowl(8,1,10);
bowl(9,1,10);
bowl(10,1,10);
bowl(11,1,10);
score(12);

document.getElementById("game").innerHTML = arrGame[9].intScore;