import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Update the HTML templates
templates = {
    "Template 1": """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{place} - {name}</title>
    <link rel="stylesheet" href="Template1.css">
</head>
<body>
    <!-- Add your content for Template 1 here -->
    <h1>تقرير التدريب التعاوني - الكلية التقنية بالمدينة المنورة</h1>
    <a href="https://tvtc.gov.sa/Style%20Library/tvtc/images/logo.svg">
      <img src="https://tvtc.gov.sa/Style%20Library/tvtc/images/logo.svg" alt="شعار الكلية التقنية بالمدينة المنورة">
    </a>
    <p>جهة التدريب: {place}</p>
    <p>الاسم: {name}</p>
    <p>التخصص: {specialization}</p>
    <p>الرقم الاكاديمي: {academic_number}</p>
    <h2>فهرس المحتويات</h2>
  <ol>
    <li><a href="#introduction">المقدمة</a></li>
    <li><a href="#company">بيان عن جهة العمل</a></li>
    <li><a href="#training-institution">جهة التدريب</a></li>
    <li><a href="#training-experience">تجربتي في التدريب</a>
      <ol>
        <li><a href="#job-description">4.1 وصف الوظيفة والمهام</a></li>
        <li><a href="#tasks-list">4.2 قائمة مفصلة بالمهام المنجزة</a></li>
        <li><a href="#equipment-description">4.3 وصف الأجهزة المستخدمة</a></li>
      </ol>
    </li>
    <li><a href="#summary">خلاصة التجربة</a></li>
    <li><a href="#recommendations">التوصيات والاقتراحات</a></li>
  </ol>

  <div class="section" id="introduction">
    <h2>المقدمة</h2>
    <p>تقدم هذه التقارير ملخصًا للتدريب التعاوني الذي قمت به في مجال الآلات والمعدات الكهربائية. تهدف التقارير إلى توضيح تفاصيل التدريب وتجاربي خلال هذه الفترة.</p>
  </div>

  
  <div class="section" id="company">
    <h2>بيان عن جهة العمل</h2>
    <p>
      اسم المنشأة: مركز التأهيل الشامل بالمدينة المنورة<br>
      طبيعة النشاط: مركز تأهيل شامل لذوي الاحتياجات الخاصة
    </p>
    <p>الأهداف:</p>
    <ul>
      <li>تقديم الرعاية والدعم والتنمية للأشخاص ذوي الإعاقة بكافة أنواعها.</li>
      <li>مساعدة الأشخاص ذوي الإعاقة على تحقيق أقصى قدر من استقلاليتهم وقدراتهم.</li>
      <li>دمج الأشخاص ذوي الإعاقة في المجتمع وسوق العمل.</li>
      <li>رفع مستوى الوعي المجتمعي بقضايا الإعاقة وحقوق الأشخاص ذوي الإعاقة.</li>
    </ul>
    <p>الهيكل التنظيمي:</p>
    <ul>
      <li>مجلس إدارة</li>
      <li>مدير عام</li>
      <li>أقسام إدارية</li>
      <li>أقسام فنية</li>
    </ul>
    <p>الفروع:</p>
    <ul>
      <li>فرع المدينة المنورة</li>
      <li>فرع جدة</li>
      <li>فرع الرياض</li>
    </ul>
    <p>بيانات وإحصائيات:</p>
    <ul>
      <li>يضم المركز أكثر من 1000 مستفيد من ذوي الإعاقة.</li>
      <li>يقدم المركز أكثر من 20 خدمة متنوعة لذوي الإعاقة.</li>
      <li>تم توظيف أكثر من 500 شخص من ذوي الإعاقة في المركز.</li>
      <li>تم تدريب أكثر من 1000 شخص من ذوي الإعاقة في المركز.</li>
      <li>تم إشراك أكثر من 500 شخص من ذوي الإعاقة في أنشطة المركز.</li>
    </ul>
  </div>

  <div class="section" id="training-institution">
    <h2>جهة التدريب</h2>
    <p>
      اسم جهة التدريب: مركز التأهيل الشامل بالمدينة المنورة<br>
      موقع جهة التدريب: المدينة المنورة، المملكة العربية السعودية<br>
      مدة التدريب: 2 أشهر
    </p>
  </div>

  <div class="section" id="training-experience">
    <h2>تجربتي في التدريب</h2>
    <div class="content">
      <h3 id="job-description">4.1 وصف الوظيفة والمهام</h3>
      <p>أثناء التدريب، قمت بالعمل كـ وصف وظيفتي  في مجال الآلات والمعدات الكهربائية:

شاركت في مشاريع مختلفة تتعلق بالصيانة والإصلاح والتركيب للآلات والمعدات الكهربائية.
تعلمت كيفية قراءة وفهم المخططات الكهربائية.
تعلمت كيفية استخدام الأدوات والمعدات الكهربائية المختلفة.
تعلمت كيفية حل الأعطال الكهربائية.
تعلمت كيفية إجراء التجارب الكهربائية.
تعلمت كيفية إعداد التقارير الفنية. حيث كانت مهامي تشمل:</p>
      <ul>
        <li>قراءة وفهم المخططات الكهربائية.</li>
        <li>تركيب وصيانة الآلات والمعدات الكهربائية.</li>
        <li>حل الأعطال الكهربائية.</li>
        <li>إجراء التجارب الكهربائية.</li>
        <li>إعداد التقارير الفنية.</li>
      </ul>

      <h3 id="tasks-list">4.2 قائمة مفصلة بالمهام المنجزة</h3>
      <ul>
        <li>تركيب وصيانة محرك كهربائي.</li>
        <li>إصلاح عطل في مولد كهربائي.</li>
        <li>إجراء تجربة لقياس شدة التيار الكهربائي.</li>
        <li>إعداد تقرير فني عن صيانة محول كهربائي.</li>
      </ul>

      <h3 id="equipment-description">4.3 وصف الأجهزة المستخدمة</h3>
      <ul>
        <li>محرك كهربائي.</li>
        <li>مولد كهربائي.</li>
        <li>محول كهربائي.</li>
        <li>مفك براغي كهربائي.</li>
        <li>سلك كهربائي.</li>
        <li>مفتاح كهربائي.</li>
        <li>مقياس كهربائي.</li>
      </ul>

      <!-- تجربتك التدريبية -->
      <h3>تجربتي التدريبية</h3>
      <p>
        خلال فترة التدريب، واجهت العديد من التحديات والفرص التي ساهمت في تطوير قدراتي ومهاراتي في مجال الآلات والمعدات الكهربائية. قمت بتنفيذ مهام متنوعة ومثيرة أسهمت في تحسين قدراتي الفنية والتقنية.
      </p>
      <p>
        إحدى أبرز التحديات التي واجهتها كانت تركيب وصيانة محرك كهربائي ضخم في مصنع صناعي. كان هذا المشروع يتطلب مهارات عالية في القراءة والتحليل للمخططات الهندسية والكهربائية. وقد استغرقت العملية وقتًا طويلاً وجهدًا كبيرًا لكن النتيجة كانت مذهلة حيث تم تشغيل المحرك بنجاح وبدأ في العمل بكفاءة عالية.
      </p>
      <p>
        كان لدي أيضًا فرصة العمل على إصلاح عطل في مولد كهربائي، وهو مشروع آخر مثير ومجزٍ. احتاجت هذه المهمة إلى دقة عالية وتركيز شديد لتحديد سبب العطل وإصلاحه بشكل صحيح. بعد جهود مكثفة، تم إصلاح المولد بنجاح وعاد للعمل بكفاءة عالية كما كان عليه قبل العطل.
      </p>
      <p>
        أيضًا، قمت بإجراء تجربة مهمة لقياس شدة التيار الكهربائي في دوائر مختلفة، وهو مشروع يتطلب دقة عالية ومعرفة جيدة بالأدوات الكهربائية. تم تنفيذ التجربة بنجاح وتم توثيق النتائج في تقرير فني دقيق.
      </p>
      <p>
        في نهاية فترة التدريب، شعرت بالرضا والفخر بما حققته من تقدم في مجال الآلات والمعدات الكهربائية. وأؤكد أن هذه التجربة كانت لا تقدر بثمن وستكون قاعدة قوية لمستقبلي المهني.
      </p>
    </div>
  </div>

  <div class="section" id="summary">
    <h2>خلاصة التجربة</h2>
    <p>إن التدريب التعاوني كان تجربة ممتازة حققت من خلالها العديد من المكتسبات والفوائد، منها:</p>
    <ul>
      <li>اكتساب مهارات عملية في مجال الآلات والمعدات الكهربائية.</li>
      <li>تطوير المهارات التحليلية والحل المشكلات.</li>
      <li>تحسين مهارات التواصل والكتابة.</li>
      <li>اكتساب المعرفة والفهم للبيئة المهنية.</li>
      <li>بناء العلاقات المهنية مع الزملاء والمدربين.</li>
    </ul>
  </div>

  <div class="section" id="recommendations">
    <h2 class="highlight">التوصيات والاقتراحات</h2>
    <ul class="recommendations">
      <li>زيادة عدد ساعات التدريب.</li>
      <li>توفير بيئة تدريبية مناسبة.</li>
      <li>تنويع المهام والتجارب التدريبية.</li>
      <li>توفير الدعم والتوجيه من قبل المدربين.</li>
      <li>تنظيم أنشطة وفعاليات اجتماعية للمتدربات.</li>
    </ul>
  </div>

  <div class="footer">
    <p>جميع الحقوق محفوظة &copy; 2023 | اسمك</p>
  </div>

</body>
</html>
""",
    "Template 2": """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{place} - {name}</title>
    <link rel="stylesheet" href="Template2.css">
</head>
<body>
    <!-- Add your content for Template 2 here -->
    <h1>تقرير التدريب التعاوني - الكلية التقنية بالمدينة المنورة</h1>
    <a href="https://tvtc.gov.sa/Style%20Library/tvtc/images/logo.svg">
      <img src="https://tvtc.gov.sa/Style%20Library/tvtc/images/logo.svg" alt="شعار الكلية التقنية بالمدينة المنورة">
    </a>
    <p>جهة التدريب: {place}</p>
    <p>الاسم: {name}</p>
    <p>التخصص: {specialization}</p>
    <p>الرقم الاكاديمي: {academic_number}</p>
    <h2>فهرس المحتويات</h2>
  <ol>
    <li><a href="#introduction">المقدمة</a></li>
    <li><a href="#company">بيان عن جهة العمل</a></li>
    <li><a href="#training-institution">جهة التدريب</a></li>
    <li><a href="#training-experience">تجربتي في التدريب</a>
      <ol>
        <li><a href="#job-description">4.1 وصف الوظيفة والمهام</a></li>
        <li><a href="#tasks-list">4.2 قائمة مفصلة بالمهام المنجزة</a></li>
        <li><a href="#equipment-description">4.3 وصف الأجهزة المستخدمة</a></li>
      </ol>
    </li>
    <li><a href="#summary">خلاصة التجربة</a></li>
    <li><a href="#recommendations">التوصيات والاقتراحات</a></li>
  </ol>

  <div class="section" id="introduction">
    <h2>المقدمة</h2>
    <p>تقدم هذه التقارير ملخصًا للتدريب التعاوني الذي قمت به في مجال الآلات والمعدات الكهربائية. تهدف التقارير إلى توضيح تفاصيل التدريب وتجاربي خلال هذه الفترة.</p>
  </div>

  
  <div class="section" id="company">
    <h2>بيان عن جهة العمل</h2>
    <p>
      اسم المنشأة: مركز التأهيل الشامل بالمدينة المنورة<br>
      طبيعة النشاط: مركز تأهيل شامل لذوي الاحتياجات الخاصة
    </p>
    <p>الأهداف:</p>
    <ul>
      <li>تقديم الرعاية والدعم والتنمية للأشخاص ذوي الإعاقة بكافة أنواعها.</li>
      <li>مساعدة الأشخاص ذوي الإعاقة على تحقيق أقصى قدر من استقلاليتهم وقدراتهم.</li>
      <li>دمج الأشخاص ذوي الإعاقة في المجتمع وسوق العمل.</li>
      <li>رفع مستوى الوعي المجتمعي بقضايا الإعاقة وحقوق الأشخاص ذوي الإعاقة.</li>
    </ul>
    <p>الهيكل التنظيمي:</p>
    <ul>
      <li>مجلس إدارة</li>
      <li>مدير عام</li>
      <li>أقسام إدارية</li>
      <li>أقسام فنية</li>
    </ul>
    <p>الفروع:</p>
    <ul>
      <li>فرع المدينة المنورة</li>
      <li>فرع جدة</li>
      <li>فرع الرياض</li>
    </ul>
    <p>بيانات وإحصائيات:</p>
    <ul>
      <li>يضم المركز أكثر من 1000 مستفيد من ذوي الإعاقة.</li>
      <li>يقدم المركز أكثر من 20 خدمة متنوعة لذوي الإعاقة.</li>
      <li>تم توظيف أكثر من 500 شخص من ذوي الإعاقة في المركز.</li>
      <li>تم تدريب أكثر من 1000 شخص من ذوي الإعاقة في المركز.</li>
      <li>تم إشراك أكثر من 500 شخص من ذوي الإعاقة في أنشطة المركز.</li>
    </ul>
  </div>

  <div class="section" id="training-institution">
    <h2>جهة التدريب</h2>
    <p>
      اسم جهة التدريب: مركز التأهيل الشامل بالمدينة المنورة<br>
      موقع جهة التدريب: المدينة المنورة، المملكة العربية السعودية<br>
      مدة التدريب: 2 أشهر
    </p>
  </div>

  <div class="section" id="training-experience">
    <h2>تجربتي في التدريب</h2>
    <div class="content">
      <h3 id="job-description">4.1 وصف الوظيفة والمهام</h3>
      <p>أثناء التدريب، قمت بالعمل كـ وصف وظيفتي  في مجال الآلات والمعدات الكهربائية:

شاركت في مشاريع مختلفة تتعلق بالصيانة والإصلاح والتركيب للآلات والمعدات الكهربائية.
تعلمت كيفية قراءة وفهم المخططات الكهربائية.
تعلمت كيفية استخدام الأدوات والمعدات الكهربائية المختلفة.
تعلمت كيفية حل الأعطال الكهربائية.
تعلمت كيفية إجراء التجارب الكهربائية.
تعلمت كيفية إعداد التقارير الفنية. حيث كانت مهامي تشمل:</p>
      <ul>
        <li>قراءة وفهم المخططات الكهربائية.</li>
        <li>تركيب وصيانة الآلات والمعدات الكهربائية.</li>
        <li>حل الأعطال الكهربائية.</li>
        <li>إجراء التجارب الكهربائية.</li>
        <li>إعداد التقارير الفنية.</li>
      </ul>

      <h3 id="tasks-list">4.2 قائمة مفصلة بالمهام المنجزة</h3>
      <ul>
        <li>تركيب وصيانة محرك كهربائي.</li>
        <li>إصلاح عطل في مولد كهربائي.</li>
        <li>إجراء تجربة لقياس شدة التيار الكهربائي.</li>
        <li>إعداد تقرير فني عن صيانة محول كهربائي.</li>
      </ul>

      <h3 id="equipment-description">4.3 وصف الأجهزة المستخدمة</h3>
      <ul>
        <li>محرك كهربائي.</li>
        <li>مولد كهربائي.</li>
        <li>محول كهربائي.</li>
        <li>مفك براغي كهربائي.</li>
        <li>سلك كهربائي.</li>
        <li>مفتاح كهربائي.</li>
        <li>مقياس كهربائي.</li>
      </ul>

      <!-- تجربتك التدريبية -->
      <h3>تجربتي التدريبية</h3>
      <p>
        خلال فترة التدريب، واجهت العديد من التحديات والفرص التي ساهمت في تطوير قدراتي ومهاراتي في مجال الآلات والمعدات الكهربائية. قمت بتنفيذ مهام متنوعة ومثيرة أسهمت في تحسين قدراتي الفنية والتقنية.
      </p>
      <p>
        إحدى أبرز التحديات التي واجهتها كانت تركيب وصيانة محرك كهربائي ضخم في مصنع صناعي. كان هذا المشروع يتطلب مهارات عالية في القراءة والتحليل للمخططات الهندسية والكهربائية. وقد استغرقت العملية وقتًا طويلاً وجهدًا كبيرًا لكن النتيجة كانت مذهلة حيث تم تشغيل المحرك بنجاح وبدأ في العمل بكفاءة عالية.
      </p>
      <p>
        كان لدي أيضًا فرصة العمل على إصلاح عطل في مولد كهربائي، وهو مشروع آخر مثير ومجزٍ. احتاجت هذه المهمة إلى دقة عالية وتركيز شديد لتحديد سبب العطل وإصلاحه بشكل صحيح. بعد جهود مكثفة، تم إصلاح المولد بنجاح وعاد للعمل بكفاءة عالية كما كان عليه قبل العطل.
      </p>
      <p>
        أيضًا، قمت بإجراء تجربة مهمة لقياس شدة التيار الكهربائي في دوائر مختلفة، وهو مشروع يتطلب دقة عالية ومعرفة جيدة بالأدوات الكهربائية. تم تنفيذ التجربة بنجاح وتم توثيق النتائج في تقرير فني دقيق.
      </p>
      <p>
        في نهاية فترة التدريب، شعرت بالرضا والفخر بما حققته من تقدم في مجال الآلات والمعدات الكهربائية. وأؤكد أن هذه التجربة كانت لا تقدر بثمن وستكون قاعدة قوية لمستقبلي المهني.
      </p>
    </div>
  </div>

  <div class="section" id="summary">
    <h2>خلاصة التجربة</h2>
    <p>إن التدريب التعاوني كان تجربة ممتازة حققت من خلالها العديد من المكتسبات والفوائد، منها:</p>
    <ul>
      <li>اكتساب مهارات عملية في مجال الآلات والمعدات الكهربائية.</li>
      <li>تطوير المهارات التحليلية والحل المشكلات.</li>
      <li>تحسين مهارات التواصل والكتابة.</li>
      <li>اكتساب المعرفة والفهم للبيئة المهنية.</li>
      <li>بناء العلاقات المهنية مع الزملاء والمدربين.</li>
    </ul>
  </div>

  <div class="section" id="recommendations">
    <h2 class="highlight">التوصيات والاقتراحات</h2>
    <ul class="recommendations">
      <li>زيادة عدد ساعات التدريب.</li>
      <li>توفير بيئة تدريبية مناسبة.</li>
      <li>تنويع المهام والتجارب التدريبية.</li>
      <li>توفير الدعم والتوجيه من قبل المدربين.</li>
      <li>تنظيم أنشطة وفعاليات اجتماعية للمتدربات.</li>
    </ul>
  </div>

  <div class="footer">
    <p>جميع الحقوق محفوظة &copy; 2023 | اسمك</p>
  </div>
</body>
</html>
""",
    "Template 3": """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{place} - {name}</title>
    <link rel="stylesheet" href="Template3.css">
</head>
<body>
    <!-- Add your content for Template 3 here -->
    <h1>تقرير التدريب التعاوني - الكلية التقنية بالمدينة المنورة</h1>
    <a href="https://tvtc.gov.sa/Style%20Library/tvtc/images/logo.svg">
      <img src="https://tvtc.gov.sa/Style%20Library/tvtc/images/logo.svg" alt="شعار الكلية التقنية بالمدينة المنورة">
    </a>
    <p>جهة التدريب: {place}</p>
    <p>الاسم: {name}</p>
    <p>التخصص: {specialization}</p>
    <p>الرقم الاكاديمي: {academic_number}</p>
    <h2>فهرس المحتويات</h2>
  <ol>
    <li><a href="#introduction">المقدمة</a></li>
    <li><a href="#company">بيان عن جهة العمل</a></li>
    <li><a href="#training-institution">جهة التدريب</a></li>
    <li><a href="#training-experience">تجربتي في التدريب</a>
      <ol>
        <li><a href="#job-description">4.1 وصف الوظيفة والمهام</a></li>
        <li><a href="#tasks-list">4.2 قائمة مفصلة بالمهام المنجزة</a></li>
        <li><a href="#equipment-description">4.3 وصف الأجهزة المستخدمة</a></li>
      </ol>
    </li>
    <li><a href="#summary">خلاصة التجربة</a></li>
    <li><a href="#recommendations">التوصيات والاقتراحات</a></li>
  </ol>

  <div class="section" id="introduction">
    <h2>المقدمة</h2>
    <p>تقدم هذه التقارير ملخصًا للتدريب التعاوني الذي قمت به في مجال الآلات والمعدات الكهربائية. تهدف التقارير إلى توضيح تفاصيل التدريب وتجاربي خلال هذه الفترة.</p>
  </div>

  
  <div class="section" id="company">
    <h2>بيان عن جهة العمل</h2>
    <p>
      اسم المنشأة: مركز التأهيل الشامل بالمدينة المنورة<br>
      طبيعة النشاط: مركز تأهيل شامل لذوي الاحتياجات الخاصة
    </p>
    <p>الأهداف:</p>
    <ul>
      <li>تقديم الرعاية والدعم والتنمية للأشخاص ذوي الإعاقة بكافة أنواعها.</li>
      <li>مساعدة الأشخاص ذوي الإعاقة على تحقيق أقصى قدر من استقلاليتهم وقدراتهم.</li>
      <li>دمج الأشخاص ذوي الإعاقة في المجتمع وسوق العمل.</li>
      <li>رفع مستوى الوعي المجتمعي بقضايا الإعاقة وحقوق الأشخاص ذوي الإعاقة.</li>
    </ul>
    <p>الهيكل التنظيمي:</p>
    <ul>
      <li>مجلس إدارة</li>
      <li>مدير عام</li>
      <li>أقسام إدارية</li>
      <li>أقسام فنية</li>
    </ul>
    <p>الفروع:</p>
    <ul>
      <li>فرع المدينة المنورة</li>
      <li>فرع جدة</li>
      <li>فرع الرياض</li>
    </ul>
    <p>بيانات وإحصائيات:</p>
    <ul>
      <li>يضم المركز أكثر من 1000 مستفيد من ذوي الإعاقة.</li>
      <li>يقدم المركز أكثر من 20 خدمة متنوعة لذوي الإعاقة.</li>
      <li>تم توظيف أكثر من 500 شخص من ذوي الإعاقة في المركز.</li>
      <li>تم تدريب أكثر من 1000 شخص من ذوي الإعاقة في المركز.</li>
      <li>تم إشراك أكثر من 500 شخص من ذوي الإعاقة في أنشطة المركز.</li>
    </ul>
  </div>

  <div class="section" id="training-institution">
    <h2>جهة التدريب</h2>
    <p>
      اسم جهة التدريب: مركز التأهيل الشامل بالمدينة المنورة<br>
      موقع جهة التدريب: المدينة المنورة، المملكة العربية السعودية<br>
      مدة التدريب: 2 أشهر
    </p>
  </div>

  <div class="section" id="training-experience">
    <h2>تجربتي في التدريب</h2>
    <div class="content">
      <h3 id="job-description">4.1 وصف الوظيفة والمهام</h3>
      <p>أثناء التدريب، قمت بالعمل كـ وصف وظيفتي  في مجال الآلات والمعدات الكهربائية:

شاركت في مشاريع مختلفة تتعلق بالصيانة والإصلاح والتركيب للآلات والمعدات الكهربائية.
تعلمت كيفية قراءة وفهم المخططات الكهربائية.
تعلمت كيفية استخدام الأدوات والمعدات الكهربائية المختلفة.
تعلمت كيفية حل الأعطال الكهربائية.
تعلمت كيفية إجراء التجارب الكهربائية.
تعلمت كيفية إعداد التقارير الفنية. حيث كانت مهامي تشمل:</p>
      <ul>
        <li>قراءة وفهم المخططات الكهربائية.</li>
        <li>تركيب وصيانة الآلات والمعدات الكهربائية.</li>
        <li>حل الأعطال الكهربائية.</li>
        <li>إجراء التجارب الكهربائية.</li>
        <li>إعداد التقارير الفنية.</li>
      </ul>

      <h3 id="tasks-list">4.2 قائمة مفصلة بالمهام المنجزة</h3>
      <ul>
        <li>تركيب وصيانة محرك كهربائي.</li>
        <li>إصلاح عطل في مولد كهربائي.</li>
        <li>إجراء تجربة لقياس شدة التيار الكهربائي.</li>
        <li>إعداد تقرير فني عن صيانة محول كهربائي.</li>
      </ul>

      <h3 id="equipment-description">4.3 وصف الأجهزة المستخدمة</h3>
      <ul>
        <li>محرك كهربائي.</li>
        <li>مولد كهربائي.</li>
        <li>محول كهربائي.</li>
        <li>مفك براغي كهربائي.</li>
        <li>سلك كهربائي.</li>
        <li>مفتاح كهربائي.</li>
        <li>مقياس كهربائي.</li>
      </ul>

      <!-- تجربتك التدريبية -->
      <h3>تجربتي التدريبية</h3>
      <p>
        خلال فترة التدريب، واجهت العديد من التحديات والفرص التي ساهمت في تطوير قدراتي ومهاراتي في مجال الآلات والمعدات الكهربائية. قمت بتنفيذ مهام متنوعة ومثيرة أسهمت في تحسين قدراتي الفنية والتقنية.
      </p>
      <p>
        إحدى أبرز التحديات التي واجهتها كانت تركيب وصيانة محرك كهربائي ضخم في مصنع صناعي. كان هذا المشروع يتطلب مهارات عالية في القراءة والتحليل للمخططات الهندسية والكهربائية. وقد استغرقت العملية وقتًا طويلاً وجهدًا كبيرًا لكن النتيجة كانت مذهلة حيث تم تشغيل المحرك بنجاح وبدأ في العمل بكفاءة عالية.
      </p>
      <p>
        كان لدي أيضًا فرصة العمل على إصلاح عطل في مولد كهربائي، وهو مشروع آخر مثير ومجزٍ. احتاجت هذه المهمة إلى دقة عالية وتركيز شديد لتحديد سبب العطل وإصلاحه بشكل صحيح. بعد جهود مكثفة، تم إصلاح المولد بنجاح وعاد للعمل بكفاءة عالية كما كان عليه قبل العطل.
      </p>
      <p>
        أيضًا، قمت بإجراء تجربة مهمة لقياس شدة التيار الكهربائي في دوائر مختلفة، وهو مشروع يتطلب دقة عالية ومعرفة جيدة بالأدوات الكهربائية. تم تنفيذ التجربة بنجاح وتم توثيق النتائج في تقرير فني دقيق.
      </p>
      <p>
        في نهاية فترة التدريب، شعرت بالرضا والفخر بما حققته من تقدم في مجال الآلات والمعدات الكهربائية. وأؤكد أن هذه التجربة كانت لا تقدر بثمن وستكون قاعدة قوية لمستقبلي المهني.
      </p>
    </div>
  </div>

  <div class="section" id="summary">
    <h2>خلاصة التجربة</h2>
    <p>إن التدريب التعاوني كان تجربة ممتازة حققت من خلالها العديد من المكتسبات والفوائد، منها:</p>
    <ul>
      <li>اكتساب مهارات عملية في مجال الآلات والمعدات الكهربائية.</li>
      <li>تطوير المهارات التحليلية والحل المشكلات.</li>
      <li>تحسين مهارات التواصل والكتابة.</li>
      <li>اكتساب المعرفة والفهم للبيئة المهنية.</li>
      <li>بناء العلاقات المهنية مع الزملاء والمدربين.</li>
    </ul>
  </div>

  <div class="section" id="recommendations">
    <h2 class="highlight">التوصيات والاقتراحات</h2>
    <ul class="recommendations">
      <li>زيادة عدد ساعات التدريب.</li>
      <li>توفير بيئة تدريبية مناسبة.</li>
      <li>تنويع المهام والتجارب التدريبية.</li>
      <li>توفير الدعم والتوجيه من قبل المدربين.</li>
      <li>تنظيم أنشطة وفعاليات اجتماعية للمتدربات.</li>
    </ul>
  </div>

  <div class="footer">
    <p>جميع الحقوق محفوظة &copy; 2023 | اسمك</p>
  </div>
</body>
</html>
""",
    "Template 4": """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{place} - {name}</title>
    <link rel="stylesheet" href="Template4.css">
</head>
<body>
    <!-- Add your content for Template 4 here -->
    <h1>تقرير التدريب التعاوني - الكلية التقنية بالمدينة المنورة</h1>
    <a href="https://tvtc.gov.sa/Style%20Library/tvtc/images/logo.svg">
      <img src="https://tvtc.gov.sa/Style%20Library/tvtc/images/logo.svg" alt="شعار الكلية التقنية بالمدينة المنورة">
    </a>
    <p>جهة التدريب: {place}</p>
    <p>الاسم: {name}</p>
    <p>التخصص: {specialization}</p>
    <p>الرقم الاكاديمي: {academic_number}</p>
    <h2>فهرس المحتويات</h2>
  <ol>
    <li><a href="#introduction">المقدمة</a></li>
    <li><a href="#company">بيان عن جهة العمل</a></li>
    <li><a href="#training-institution">جهة التدريب</a></li>
    <li><a href="#training-experience">تجربتي في التدريب</a>
      <ol>
        <li><a href="#job-description">4.1 وصف الوظيفة والمهام</a></li>
        <li><a href="#tasks-list">4.2 قائمة مفصلة بالمهام المنجزة</a></li>
        <li><a href="#equipment-description">4.3 وصف الأجهزة المستخدمة</a></li>
      </ol>
    </li>
    <li><a href="#summary">خلاصة التجربة</a></li>
    <li><a href="#recommendations">التوصيات والاقتراحات</a></li>
  </ol>

  <div class="section" id="introduction">
    <h2>المقدمة</h2>
    <p>تقدم هذه التقارير ملخصًا للتدريب التعاوني الذي قمت به في مجال الآلات والمعدات الكهربائية. تهدف التقارير إلى توضيح تفاصيل التدريب وتجاربي خلال هذه الفترة.</p>
  </div>

  
  <div class="section" id="company">
    <h2>بيان عن جهة العمل</h2>
    <p>
      اسم المنشأة: مركز التأهيل الشامل بالمدينة المنورة<br>
      طبيعة النشاط: مركز تأهيل شامل لذوي الاحتياجات الخاصة
    </p>
    <p>الأهداف:</p>
    <ul>
      <li>تقديم الرعاية والدعم والتنمية للأشخاص ذوي الإعاقة بكافة أنواعها.</li>
      <li>مساعدة الأشخاص ذوي الإعاقة على تحقيق أقصى قدر من استقلاليتهم وقدراتهم.</li>
      <li>دمج الأشخاص ذوي الإعاقة في المجتمع وسوق العمل.</li>
      <li>رفع مستوى الوعي المجتمعي بقضايا الإعاقة وحقوق الأشخاص ذوي الإعاقة.</li>
    </ul>
    <p>الهيكل التنظيمي:</p>
    <ul>
      <li>مجلس إدارة</li>
      <li>مدير عام</li>
      <li>أقسام إدارية</li>
      <li>أقسام فنية</li>
    </ul>
    <p>الفروع:</p>
    <ul>
      <li>فرع المدينة المنورة</li>
      <li>فرع جدة</li>
      <li>فرع الرياض</li>
    </ul>
    <p>بيانات وإحصائيات:</p>
    <ul>
      <li>يضم المركز أكثر من 1000 مستفيد من ذوي الإعاقة.</li>
      <li>يقدم المركز أكثر من 20 خدمة متنوعة لذوي الإعاقة.</li>
      <li>تم توظيف أكثر من 500 شخص من ذوي الإعاقة في المركز.</li>
      <li>تم تدريب أكثر من 1000 شخص من ذوي الإعاقة في المركز.</li>
      <li>تم إشراك أكثر من 500 شخص من ذوي الإعاقة في أنشطة المركز.</li>
    </ul>
  </div>

  <div class="section" id="training-institution">
    <h2>جهة التدريب</h2>
    <p>
      اسم جهة التدريب: مركز التأهيل الشامل بالمدينة المنورة<br>
      موقع جهة التدريب: المدينة المنورة، المملكة العربية السعودية<br>
      مدة التدريب: 2 أشهر
    </p>
  </div>

  <div class="section" id="training-experience">
    <h2>تجربتي في التدريب</h2>
    <div class="content">
      <h3 id="job-description">4.1 وصف الوظيفة والمهام</h3>
      <p>أثناء التدريب، قمت بالعمل كـ وصف وظيفتي  في مجال الآلات والمعدات الكهربائية:

شاركت في مشاريع مختلفة تتعلق بالصيانة والإصلاح والتركيب للآلات والمعدات الكهربائية.
تعلمت كيفية قراءة وفهم المخططات الكهربائية.
تعلمت كيفية استخدام الأدوات والمعدات الكهربائية المختلفة.
تعلمت كيفية حل الأعطال الكهربائية.
تعلمت كيفية إجراء التجارب الكهربائية.
تعلمت كيفية إعداد التقارير الفنية. حيث كانت مهامي تشمل:</p>
      <ul>
        <li>قراءة وفهم المخططات الكهربائية.</li>
        <li>تركيب وصيانة الآلات والمعدات الكهربائية.</li>
        <li>حل الأعطال الكهربائية.</li>
        <li>إجراء التجارب الكهربائية.</li>
        <li>إعداد التقارير الفنية.</li>
      </ul>

      <h3 id="tasks-list">4.2 قائمة مفصلة بالمهام المنجزة</h3>
      <ul>
        <li>تركيب وصيانة محرك كهربائي.</li>
        <li>إصلاح عطل في مولد كهربائي.</li>
        <li>إجراء تجربة لقياس شدة التيار الكهربائي.</li>
        <li>إعداد تقرير فني عن صيانة محول كهربائي.</li>
      </ul>

      <h3 id="equipment-description">4.3 وصف الأجهزة المستخدمة</h3>
      <ul>
        <li>محرك كهربائي.</li>
        <li>مولد كهربائي.</li>
        <li>محول كهربائي.</li>
        <li>مفك براغي كهربائي.</li>
        <li>سلك كهربائي.</li>
        <li>مفتاح كهربائي.</li>
        <li>مقياس كهربائي.</li>
      </ul>

      <!-- تجربتك التدريبية -->
      <h3>تجربتي التدريبية</h3>
      <p>
        خلال فترة التدريب، واجهت العديد من التحديات والفرص التي ساهمت في تطوير قدراتي ومهاراتي في مجال الآلات والمعدات الكهربائية. قمت بتنفيذ مهام متنوعة ومثيرة أسهمت في تحسين قدراتي الفنية والتقنية.
      </p>
      <p>
        إحدى أبرز التحديات التي واجهتها كانت تركيب وصيانة محرك كهربائي ضخم في مصنع صناعي. كان هذا المشروع يتطلب مهارات عالية في القراءة والتحليل للمخططات الهندسية والكهربائية. وقد استغرقت العملية وقتًا طويلاً وجهدًا كبيرًا لكن النتيجة كانت مذهلة حيث تم تشغيل المحرك بنجاح وبدأ في العمل بكفاءة عالية.
      </p>
      <p>
        كان لدي أيضًا فرصة العمل على إصلاح عطل في مولد كهربائي، وهو مشروع آخر مثير ومجزٍ. احتاجت هذه المهمة إلى دقة عالية وتركيز شديد لتحديد سبب العطل وإصلاحه بشكل صحيح. بعد جهود مكثفة، تم إصلاح المولد بنجاح وعاد للعمل بكفاءة عالية كما كان عليه قبل العطل.
      </p>
      <p>
        أيضًا، قمت بإجراء تجربة مهمة لقياس شدة التيار الكهربائي في دوائر مختلفة، وهو مشروع يتطلب دقة عالية ومعرفة جيدة بالأدوات الكهربائية. تم تنفيذ التجربة بنجاح وتم توثيق النتائج في تقرير فني دقيق.
      </p>
      <p>
        في نهاية فترة التدريب، شعرت بالرضا والفخر بما حققته من تقدم في مجال الآلات والمعدات الكهربائية. وأؤكد أن هذه التجربة كانت لا تقدر بثمن وستكون قاعدة قوية لمستقبلي المهني.
      </p>
    </div>
  </div>

  <div class="section" id="summary">
    <h2>خلاصة التجربة</h2>
    <p>إن التدريب التعاوني كان تجربة ممتازة حققت من خلالها العديد من المكتسبات والفوائد، منها:</p>
    <ul>
      <li>اكتساب مهارات عملية في مجال الآلات والمعدات الكهربائية.</li>
      <li>تطوير المهارات التحليلية والحل المشكلات.</li>
      <li>تحسين مهارات التواصل والكتابة.</li>
      <li>اكتساب المعرفة والفهم للبيئة المهنية.</li>
      <li>بناء العلاقات المهنية مع الزملاء والمدربين.</li>
    </ul>
  </div>

  <div class="section" id="recommendations">
    <h2 class="highlight">التوصيات والاقتراحات</h2>
    <ul class="recommendations">
      <li>زيادة عدد ساعات التدريب.</li>
      <li>توفير بيئة تدريبية مناسبة.</li>
      <li>تنويع المهام والتجارب التدريبية.</li>
      <li>توفير الدعم والتوجيه من قبل المدربين.</li>
      <li>تنظيم أنشطة وفعاليات اجتماعية للمتدربات.</li>
    </ul>
  </div>

  <div class="footer">
    <p>جميع الحقوق محفوظة &copy; 2023 | اسمك</p>
  </div>
</body>
</html>
""",
    "Template 5": """
"""
}


def save_report_to_file():
    # Get the selected template and the input values
    selected_template = template_combobox.get()
    place = place_entry.get()
    name = name_entry.get()
    specialization = specialization_entry.get()
    academic_number = academic_number_entry.get()

    # Get the HTML template based on the selected template
    html_template = templates.get(selected_template, "")

    # Replace the placeholders with the input values
    html_template = html_template.replace("{place}", place)
    html_template = html_template.replace("{name}", name)
    html_template = html_template.replace("{specialization}", specialization)
    html_template = html_template.replace("{academic_number}", academic_number)

    # Open a file dialog to save the report
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(html_template)
            messagebox.showinfo("Success", "The report has been saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the report: {e}")


# Create the main window
root = tk.Tk()
root.title("Internship Report Generator")
root.geometry("400x400")

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

template_label = ttk.Label(frame, text="Select Template:")
template_label.pack()

template_combobox = ttk.Combobox(frame, values=list(templates.keys()))
template_combobox.pack()

place_label = ttk.Label(frame, text="Place of Training:")
place_label.pack()
place_entry = ttk.Entry(frame)
place_entry.pack()

name_label = ttk.Label(frame, text="Your Name:")
name_label.pack()
name_entry = ttk.Entry(frame)
name_entry.pack()

specialization_label = ttk.Label(frame, text="Your Specialization:")
specialization_label.pack()
specialization_entry = ttk.Entry(frame)
specialization_entry.pack()

academic_number_label = ttk.Label(frame, text="Your Academic Number:")
academic_number_label.pack()
academic_number_entry = ttk.Entry(frame)
academic_number_entry.pack()

generate_button = ttk.Button(frame, text="Generate Report", command=save_report_to_file)
generate_button.pack()

root.mainloop()