<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>전가산기 회로도</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        
        .container {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }
        
        svg {
            background: #1a2332;
            border-radius: 10px;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        
        .wire {
            fill: none;
            stroke: #00d4ff;
            stroke-width: 2.5;
            stroke-linecap: round;
        }
        
        .gate {
            fill: #2d3e50;
            stroke: #00d4ff;
            stroke-width: 2;
        }
        
        .gate-text {
            fill: #00d4ff;
            font-size: 16px;
            font-weight: bold;
            font-family: 'Courier New', monospace;
        }
        
        .label {
            fill: #ffffff;
            font-size: 18px;
            font-weight: bold;
            font-family: 'Segoe UI', sans-serif;
        }
        
        .input-point {
            fill: #00d4ff;
            stroke: #ffffff;
            stroke-width: 1;
        }
        
        .output-point {
            fill: #ff6b35;
            stroke: #ffffff;
            stroke-width: 1;
        }
    </style>
</head>
<body>
    <div class="container">
        <svg width="600" height="400" viewBox="0 0 600 400">
            <!-- 입력 라벨 -->
            <text x="30" y="50" class="label">A</text>
            <text x="30" y="110" class="label">B</text>
            <text x="20" y="200" class="label">Ci</text>
            
            <!-- 출력 라벨 -->
            <text x="540" y="90" class="label">S1</text>
            <text x="520" y="250" class="label">Carry</text>
            
            <!-- 입력 포인트 -->
            <circle cx="60" cy="45" r="4" class="input-point"/>
            <circle cx="60" cy="105" r="4" class="input-point"/>
            <circle cx="60" cy="195" r="4" class="input-point"/>
            
            <!-- XOR 게이트 (상단) -->
            <path d="M 150 25 Q 160 25 170 35 L 170 75 Q 160 85 150 85 Q 165 55 150 25" class="gate"/>
            <path d="M 145 25 Q 160 55 145 85" class="gate" fill="none"/>
            <text x="155" y="60" class="gate-text">XOR</text>
            
            <!-- XOR 입력선 -->
            <path d="M 60 45 L 150 45" class="wire"/>
            <path d="M 60 105 L 120 105 L 120 65 L 150 65" class="wire"/>
            
            <!-- XOR 출력선 -->
            <path d="M 170 55 L 250 55" class="wire"/>
            
            <!-- AND 게이트 (하단 좌측) -->
            <path d="M 150 180 L 150 220 Q 150 240 170 240 Q 190 240 190 220 L 190 180 Z" class="gate"/>
            <text x="155" y="215" class="gate-text">AND</text>
            
            <!-- AND 입력선 (하단 좌측) -->
            <path d="M 60 45 L 60 190 L 150 190" class="wire"/>
            <path d="M 120 105 L 120 210 L 150 210" class="wire"/>
            
            <!-- AND 출력선 (하단 좌측) -->
            <path d="M 190 200 L 250 200" class="wire"/>
            
            <!-- AND 게이트 (중앙) -->
            <path d="M 320 40 L 320 100 Q 320 120 340 120 Q 360 120 360 100 L 360 40 Z" class="gate"/>
            <text x="325" y="85" class="gate-text">AND</text>
            
            <!-- AND 입력선 (중앙) -->
            <path d="M 250 55 L 320 55" class="wire"/>
            <path d="M 60 195 L 280 195 L 280 85 L 320 85" class="wire"/>
            
            <!-- AND 출력선 (중앙) -->
            <path d="M 360 70 L 420 70" class="wire"/>
            
            <!-- OR 게이트 -->
            <path d="M 420 50 Q 430 50 445 65 L 445 95 Q 430 110 420 110 Q 435 80 420 50" class="gate"/>
            <path d="M 415 50 Q 430 80 415 110" class="gate" fill="none"/>
            <text x="425" y="85" class="gate-text">OR</text>
            
            <!-- OR 입력선 -->
            <path d="M 420 65 L 420 65" class="wire"/>
            <path d="M 250 200 L 380 200 L 380 95 L 420 95" class="wire"/>
            
            <!-- OR 출력선 (Carry) -->
            <path d="M 445 80 L 510 80 L 510 245 L 520 245" class="wire"/>
            <circle cx="520" cy="245" r="4" class="output-point"/>
            
            <!-- S1 출력선 -->
            <path d="M 250 55 L 530 55 L 530 85 L 540 85" class="wire"/>
            <circle cx="540" cy="85" r="4" class="output-point"/>
            
            <!-- 연결 포인트 -->
            <circle cx="60" cy="45" r="3" fill="#00d4ff"/>
            <circle cx="120" cy="105" r="3" fill="#00d4ff"/>
            <circle cx="280" cy="195" r="3" fill="#00d4ff"/>
            <circle cx="250" cy="55" r="3" fill="#00d4ff"/>
            <circle cx="250" cy="200" r="3" fill="#00d4ff"/>
        </svg>
    </div>
</body>
</html>