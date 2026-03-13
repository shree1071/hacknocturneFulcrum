# 🎯 Winning the $100 Requestly Partner Track

The Requestly JSON bulk importer currently has a known bug parsing large APIs. **However, bulk importing basic endpoints won't win the "Most Creative Use" prize anyway.** 

To win the $100 partner track, you need to showcase Requestly's powerful **HTTP Rules** and **Mocking** engine to simulate real-world medical/blockchain edge cases during your demo. 

Here are **3 creative Requestly HTTP Rules** to configure manually. These take 2 minutes to set up and will impress the judges by proving your app is robust.

---

### Rule 1: The "Blockchain Congestion" Simulator (Network Delay Rule)
*Show the judges your UI handles slow smart contract confirmations gracefully via loading states.*

1. Open Requestly → **HTTP Rules** → **New Rule**
2. Select **Delay Network Request**
3. **Condition:** If URL `Matches (Regex)` `.*api/records/.*` OR URL `Matches (Regex)` `.*api/access-grants.*`
4. **Action:** Delay the request by `3000` milliseconds (3 seconds).
5. **Name it:** `Simulate Blockchain Congestion`
6. **Demo Effect:** When you grant a doctor access on the frontend, the UI will show its loading spinner for 3 seconds before succeeding, proving you aren't just faking instantaneous transactions.

---

### Rule 2: The "Tavus Wait-Time Bypass" (API Mocking / Modify API Response)
*Tavus AI video generation takes 5-10 minutes. Use Requestly to mock it for an instant live demo.*

1. Open Requestly → **HTTP Rules** → **New Rule**
2. Select **Modify API Response** (Local Mock)
3. **Condition:** If URL `Contains` `api/tavus-video` AND Method is `GET`
4. **Response Body:** Replace existing response with Static Data:
   ```json
   {
      "video_id": "test_video_123",
      "status": "completed",
      "download_url": "https://www.w3schools.com/html/mov_bbb.mp4" 
   }
   ```
5. **Name it:** `Mock Tavus Video Completion`
6. **Demo Effect:** Instead of the judges waiting 10 minutes for Tavus to render a CVI video, your polling endpoint instantly hits this Requestly mock, and your frontend immediately plays the (placeholder) video.

---

### Rule 3: The "Zero-Knowledge Offline Fallback" (Modify Headers)
*Show how your system protects patient privacy even if the auth token drops.*

1. Open Requestly → **HTTP Rules** → **New Rule**
2. Select **Modify Headers**
3. **Condition:** If URL `Contains` `/api/records/` AND Method is `GET`
4. **Action:** `Remove` Request Header -> `Authorization`
5. **Name it:** `Drop Auth Headers (Chaos Test)`
6. **Demo Effect:** Toggle this rule ON during the demo and refresh the page. Show the judges that your Python backend correctly catches the missing auth and returns a 401 Unauthorized, and that your frontend gracefully redirects to the MetaMask login screen instead of crashing.

---

### 🚀 How to Pitch This to Judges:

> *"We used Requestly not just as an API client, but as a Chaos Engineering tool. We built HTTP Rules to inject 3-second network delays to simulate blockchain finality times, ensuring our frontend loading states protect against double-spending. We also used Requestly's Local Response Mocking to instantly resolve the 10-minute Tavus AI video generation during demos, and injected missing Auth headers to prove our Zero-Knowledge RBAC system halts unauthorized access securely."*
