import shutil

s = input("What version? ")
source_dir = r"{}".format(s)
destination_dir = r"{}_particles".format(s)
shutil.copytree(source_dir, destination_dir)

html_files = ['{}/home.html'.format(destination_dir),'{}/index.html'.format(destination_dir)]

css_files = ['{}/home.css'.format(destination_dir)]




for curr_file in html_files:

  with open(curr_file, 'r') as file :
    filedata = file.read()

  footer= '''    <section class="u-backlink u-clearfix u-grey-80">
      <a class="u-link" href="https://nicepage.com/website-templates" target="_blank">
        <span>Website Templates</span>
      </a>
      <p class="u-text">
        <span>created with</span>
      </p>
      <a class="u-link" href="https://nicepage.com/" target="_blank">
        <span>Website Builder Software</span>
      </a>.
    </section>'''
  no_footer = "<!-- Succesfully removed -->"

  filedata = filedata.replace(footer, no_footer)
  
  print('Footer succesfully removed in {}!'.format(curr_file))
  
  old_section = '''    <section class="u-clearfix u-gradient u-section-1" id="sec-a868">
      <div class="u-clearfix u-sheet u-valign-middle u-sheet-1">
        <div class="u-clearfix u-expanded-width u-gutter-0 u-layout-wrap u-layout-wrap-1">
          <div class="u-gutter-0 u-layout">
            <div class="u-layout-row">
              <div class="u-align-center u-container-style u-gradient u-layout-cell u-size-60 u-layout-cell-1">
                <div class="u-container-layout u-container-layout-1">
                  <h2 class="u-align-center u-custom-font u-font-roboto-slab u-text u-text-body-alt-color u-text-1" data-animation-name="fadeIn" data-animation-duration="1750" data-animation-delay="0" data-animation-direction="Up">antonio foglia.<span style="font-weight: 700;">
                      <span style="font-weight: 400;"></span>
                    </span>
                  </h2>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''
  
  new_section_with_particles ='''    <!-- BEGIN PART EDITED BY ME -->
    <section class="u-clearfix u-gradient u-section-1" id="particles-js">

      <script src="particles/js/particles.js"></script>
      <script src="particles/js/app.js"></script>

      <div style="position: absolute; display: block; margin: 0; padding: 0; top: 40%; left: 50%; transform: translate3d(-50%,-50%,0); color: white; text-align: center!important;">
        <h2 class="u-custom-font u-font-roboto-slab u-text u-text-body-alt-color u-text-1" data-animation-name="fadeIn" data-animation-duration="1750" data-animation-delay="0" data-animation-direction="Up">antonio foglia.<span style="font-weight: 700;">
            <span style="font-weight: 400;"></span>
          </span>
        </h2>
      </div>
    </section>
    <!-- END PART EDITED BY ME -->'''
  
  filedata = filedata.replace(old_section, new_section_with_particles)
  
  print('Particles succesfully added in {}!'.format(curr_file))

  with open(curr_file, 'w') as file:
    file.write(filedata)
    
    
for curr_file in css_files:
  
  css_text='''
  
/* BEGIN MYSTUFF */

html_particle,body_particle{
	width:100%;
	height:100%;
	background:#000000;
}

#particles-js{
  width: 100%;
  height: 100%;
  background-color: #000000;
  background-image: url('');
  background-size: cover;
  background-position: 50% 50%;
  background-repeat: no-repeat;
}

#div_particle{
  text-align: center;
  align-items: center;
}
'''

  with open(curr_file, 'a') as file :
    file.write(css_text)
    
  print('CSS succesfully appended in {}!'.format(curr_file))







