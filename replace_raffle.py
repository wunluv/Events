import re

with open('Mabon/index.html', 'r') as f:
    content = f.read()

# We want to replace everything from `<div class="mt-10 grid gap-8 lg:grid-cols-[0.95fr_1.05fr] lg:items-start">`
# to `</div>` just before `<!-- Prize Cards -->`

start_marker = r'<div class="mt-10 grid gap-8 lg:grid-cols-\[0\.95fr_1\.05fr\] lg:items-start">'
end_marker = r'<!-- Prize Cards -->'

pattern = re.compile(start_marker + r'.*?</div>\s+(?=' + end_marker + r')', re.DOTALL)

replacement = """<div class="mt-10">
                    <div class="space-y-6 rounded-[2rem] border border-mabon-oat/60 bg-white/85 p-8 shadow-card backdrop-blur">
                        <p class="font-display text-3xl text-mabon-dusk">Congratulations to:</p>
                        <ol class="mt-4 space-y-4 text-lg leading-7 text-mabon-dusk/78">
                            <li class="flex items-center gap-3"><span class="flex h-8 w-8 items-center justify-center rounded-full bg-mabon-saffron text-white font-bold">1</span> <span class="font-semibold text-mabon-dusk">Morne Red Clay, Hogsback</span> - 1st Prize</li>
                            <li class="flex items-center gap-3"><span class="flex h-8 w-8 items-center justify-center rounded-full bg-mabon-saffron/80 text-white font-bold">2</span> <span class="font-semibold text-mabon-dusk">Serge Sweet grass Raw, Hogsback</span> - 2nd Prize</li>
                            <li class="flex items-center gap-3"><span class="flex h-8 w-8 items-center justify-center rounded-full bg-mabon-saffron/60 text-white font-bold">3</span> <span class="font-semibold text-mabon-dusk">Wendy Retief, Hogsback</span> - 3rd Prize</li>
                            <li class="flex items-center gap-3"><span class="flex h-8 w-8 items-center justify-center rounded-full bg-mabon-parchment text-mabon-dusk font-bold">4</span> <span class="font-semibold text-mabon-dusk">Natalie van Rooyen, PE</span> - 4th Prize</li>
                            <li class="flex items-center gap-3"><span class="flex h-8 w-8 items-center justify-center rounded-full bg-mabon-parchment text-mabon-dusk font-bold">5</span> <span class="font-semibold text-mabon-dusk">Linda Rautenbach, Hogsback</span> - 5th Prize</li>
                            <li class="flex items-center gap-3"><span class="flex h-8 w-8 items-center justify-center rounded-full bg-mabon-parchment text-mabon-dusk font-bold">6</span> <span class="font-semibold text-mabon-dusk">Nadia Schenk, Hogsback</span> - 6th Prize</li>
                        </ol>
                    </div>
                </div>

                """

# Also update the title
content = content.replace(
    '<h2 id="raffle-heading" class="font-display type-h1 mt-5 text-mabon-dusk">Revelous Roof Raffle prize winners announced on 17th at Stella\'s farewell party</h2>',
    '<h2 id="raffle-heading" class="font-display type-h1 mt-5 text-mabon-dusk">Revelous Roof Raffle prize winners</h2>'
)

new_content, count = pattern.subn(replacement, content)
print(f"Replaced {count} instances.")

with open('Mabon/index.html', 'w') as f:
    f.write(new_content)

